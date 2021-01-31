"""
A wrapper around the Hack the Box API
"""
import requests
from htb import HTB, HTBAPIError


__version__ = '1.1.5'

class HTBCLIError(HTBAPIError):
    """Raised when API fails"""
    def __init__(self, expression, message=""):
        self.expression = expression
        self.message = message

class HTBAPI(HTB):
    """
    Extends Hack the Box API Wrapper

    :attr api_key: API Key used for authenticated queries
    :attr user_agent: The User-Agent to be used with all requests
    """

    def __init__(self, api_key, user_agent='Python HTB Client/{}'.format(__version__)):
        HTB.__init__(self, api_key, user_agent)
        self.headers['Authorization'] = f"Bearer {api_key}"
        HTB._validate_response = HTBAPI._validate_response

    @staticmethod
    def _validate_response(response):
        """
        Overridden to implement additional error message
        Validate the response from the API

        :params response: the response dict received from an API call
        :returns: the response dict if the call was successfull
        """
        if "success" in response and response['success'] != '1' and response['success'] != 1:
            message = "\n".join([ f"{k}: {v}" for k,v in response.items() ])
            raise HTBCLIError("success != 1", message=message)
        return response

    def get_owns(self) -> dict:
        """
        Get which machines the user has owned.

        :params self: HTB object in use
        :returns: machines dict
        """
        return requests.get(self.BASE_URL + self._auth('/machines/owns'), headers=self.headers).json()

    def get_assigned(self) -> dict:
        """
        Get which machines the user has assigned to them.

        :params self: HTB object in use
        :returns: machines dict

        VIP Only
        """
        return requests.get(self.BASE_URL + self._auth('/machines/assigned'), headers=self.headers).json()

    def get_difficulties(self) -> dict:
        """
        Get machines difficulty.

        :params self: HTB object in use
        :returns: machines dict
        """
        return requests.get(self.BASE_URL + self._auth('/machines/difficulty'), headers=self.headers).json()

    
    def spawn_machine(self, mid: int, lab="vip") -> (int, str):
        """
        Spawn a machine

        :params self: HTB object in use
        :params mid: Machine ID or 0 for arena.
        :params lab: vip for vip users, unknown for free.
        :returns: bool if successful, str status message
        """
        try:
            if mid == 0:
                resp = self._get('/machines/release/spawn')
            else:
                resp = self._post(self._auth('/vm/{}/assign/{}'.format(lab, mid)))
            status = resp['status'] if 'status' is resp else resp['message']
            return (resp['success'], status)
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"
    
    def terminate_machine(self, mid: int, lab="vip") -> (int, str):
        """
        Terminate a machine

        :params self: HTB object in use
        :params mid: Machine ID or 0 for arena
        :params lab: vip for vip users, unknown for free.
        :returns: bool if successful, str status message
        """
        try:
            if mid == 0:
                resp = self._get('/machines/release/terminate')
            else:
                resp = self._post(self._auth('/vm/{}/remove/{}'.format(lab, mid)))
            status = resp['status'] if 'status' is resp else resp['message']
            return (resp['success'], status)
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"
    
    def own_machine(self, mid: int, hsh: str, diff: int) -> (int, str):
        """
        Own a challenge on a machine

        :params self: HTB object in use
        :params mid: Machine ID or 0 for arena
        :params hsh: Flag Hash
        :params diff: difficult (10-100)
        :returns: bool if successful
        """
        try:
            endpoint = "/machines/release/own" if mid == 0 else '/machines/own'
            resp = self._post(self._auth(endpoint), {"id": mid, "flag": hsh, "difficulty": diff})
            status = resp['status'] if 'status' is resp else resp['message']
            return (resp['success'], status)
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"

    def reset_machine(self, mid: int) -> dict:
        """
        Reset a machine

        :params self: HTB object in use
        :params mid: Machine ID or 0 for arena
        :returns: dict of info
        """
        try:
            if mid == 0:
                resp = self._get('/machines/release/reset')
            else:
                resp = super().reset_machine(mid)
            return resp
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"

    def arena_stats(self) -> dict:
        """
        Get arena stats.

        :params self: HTB object in use
        :returns: dict of arena info.
        """
        try:
            return self._get('/machines/release/stats')
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred" 

    def arena_owns(self, mid: int) -> dict:
        """
        Get arena machine own info.

        :params self: HTB object in use
        :params mid: Machine ID
        :returns: dict of info
        """
        try:
            resp = self._get(f"/machines/release/owns/{mid}")
            return resp["owns"]
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"

    def active_arena(self) -> dict:
        """
        Get active arena machine info.

        :params self: HTB object in use
        :returns: dict of info
        """
        try:
            resp = self._get(f"/machines/release/active")
            return resp
        except HTBAPIError as e:
            print(e.message)
            return {'spawned': False}

    def select_arena(self, region:str) -> bool:
        """
        Select arena region.

        :params self: HTB object in use
        :params region: us | eu.
        :returns: bool success
        """
        try:
            resp = self._post(self._auth(f"/labs/switch/{region.lower()}release"))
            return resp['status'] == 1
        except HTBAPIError as e:
            print(e.message)
            return False

