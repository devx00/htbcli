"""
A wrapper around the Hack the Box API
"""
import requests
from htb import HTB, HTBAPIError


__version__ = '1.1.3'

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
        if response['success'] != '1' and response['success'] != 1:
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
        :params mid: Machine ID
        :params lab: vip for vip users, unknown for free.
        :returns: bool if successful, str status message
        """
        try:
            resp = self._post(self._auth('/vm/{}/assign/{}'.format(lab, mid)))
            return (resp['success'], resp['status'])
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"
    
    def terminate_machine(self, mid: int, lab="vip") -> (int, str):
        """
        Terminate a machine

        :params self: HTB object in use
        :params mid: Machine ID
        :params lab: vip for vip users, unknown for free.
        :returns: bool if successful, str status message
        """
        try:
            resp = self._post(self._auth('/vm/{}/remove/{}'.format(lab, mid)))
            return (resp['success'], resp['status'])
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"
    
    def own_machine(self, mid: int, hsh: str, diff: int) -> (int, str):
        """
        Own a challenge on a machine

        :params self: HTB object in use
        :params mid: Machine ID
        :params hsh: Flag Hash
        :params diff: difficult (10-100)
        :returns: bool if successful
        """
        try:
            resp = self._post(self._auth('/machines/own'), {"id": mid, "flag": hsh, "difficulty": diff})
            return (resp['success'], resp['status'])
        except HTBAPIError as e:
            print(e.message)
            return False, "An Error Occurred"
