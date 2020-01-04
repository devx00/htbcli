Hack the Box CLI
================

Just a small tool I threw together one day to make it easy to work with HTB from the command line. It uses the [API wrapper](https://github.com/kulinacs/htb) from @kulinacs with a few modifications.

Usage
--------

**Install**

```bash
pip install htbcli
```

**Config**

after installing the module. configure it with
```bash
# For free users use this command. 
# Replace [your_key] with your actual api key from the settings page on HTB.
htb config --lab=free --apiKey=[your_key]

# For VIP Users its the same just pass vip instead of free to the --lab argument.
htb config --lab=vip --apiKey=[your_key]
```

**List**

You can list all the boxes on HTB. Just use the list command.
```bash
$ htb list -h
# usage: htb list [-h] [--retired] [--assigned] [--incomplete] [--sort-by field]
#                 [--reverse] [-s SEPARATOR] [-rs ROW_SEPARATOR] [-q]
#                 [-f field [field ...]] [-a]

# optional arguments:
#   -h, --help            show this help message and exit
#   --retired             Include retired boxes in the output. [NOTE: Retired
#                         boxes are only available to VIP users and cannot be
#                         accessed by a free user.]
#   --assigned            Show what machines are assigned to you. [VIP Only]
#   --incomplete          Only show incomplete boxes in the output. An
#                         incomplete box is one where you haven't owned both
#                         user and root.
#   --sort-by field       Field to sort by. This will sort the boxes by the
#                         passed field. You can reverse the order by passing
#                         --reverse. Certain fields like difficulty will be the
#                         average value. To sort by the official HTB rank (ie
#                         easy/medium/hard) sort by the amount of points the box
#                         is/was assigned.
#   --reverse             Reverse the order of boxes. This will return the list
#                         sorted by the sort field in reverse.
#   -s SEPARATOR, --separator SEPARATOR
#                         The separator to use when outputting the fields when
#                         -q is set
#   -rs ROW_SEPARATOR, --row-separator ROW_SEPARATOR
#                         The separator to use between rows when outputting the
#                         fields when -q is set
#   -q, --quiet           Output only the field values without any formatting.
#                         Useful when parsing the output.
#   -f field [field ...], --fields field [field ...]
#                         Limit the output to only these fields. All fields
#                         shown when this is omitted.
#   -a, --all-fields      Output every field on the machines.


$ htb list
# ╒══════╤════════════╤═════════╤══════════╤══════════════╤══════════════╤══════════╕
# │   id │ name       │ os      │   rating │ owned_user   │ owned_root   │ active   │
# ╞══════╪════════════╪═════════╪══════════╪══════════════╪══════════════╪══════════╡
# │  191 │ Smasher2   │ Linux   │      4.4 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  193 │ Chainsaw   │ Linux   │      4.2 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  196 │ Player     │ Linux   │      4.8 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  197 │ Craft      │ Linux   │      4.9 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  198 │ RE         │ Windows │      4.4 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  200 │ Rope       │ Linux   │      4.7 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  201 │ Heist      │ Windows │      4.4 │ True         │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  202 │ Scavenger  │ Linux   │      3.3 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  203 │ Networked  │ Linux   │      3.7 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  204 │ Zetta      │ Linux   │      4.5 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  207 │ Bitlab     │ Linux   │      3.7 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  208 │ Wall       │ Linux   │      2.3 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  209 │ Bankrobber │ Windows │      2.7 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  210 │ Json       │ Windows │      4.1 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  211 │ Sniper     │ Windows │      4.5 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  212 │ Forest     │ Windows │      4.6 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  213 │ Registry   │ Linux   │      4.4 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  214 │ Mango      │ Linux   │      3.8 │ True         │ True         │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  215 │ Postman    │ Linux   │      3.9 │ False        │ False        │ True     │
# ├──────┼────────────┼─────────┼──────────┼──────────────┼──────────────┼──────────┤
# │  216 │ AI         │ Linux   │      2.7 │ False        │ False        │ True     │
# ╘══════╧════════════╧═════════╧══════════╧══════════════╧══════════════╧══════════╛


```


**Info**

You can see data on a single machine with the info command.

```bash
$ htb info -h
# usage: htb info [-h] [-s SEPARATOR] [-q] [-f field [field ...]] [-a] BOX

# positional arguments:
#   BOX                   The name of the box you want info for.

# optional arguments:
#   -h, --help            show this help message and exit
#   -s SEPARATOR, --separator SEPARATOR
#                         The separator to use when outputting the fields when
#                         -q is set
#   -q, --quiet           Output only the field values without any formatting.
#                         Useful when parsing the output.
#   -f field [field ...], --fields field [field ...]
#                         Limit the output to only these fields. All fields
#                         shown when this is omitted.
#   -a, --all-fields      Output every field on the machine.


$ htb info lame
# ╒═══════════════╤══════════════════════════════════════════════════════════════════════════════════════╕
# │ id            │ 1                                                                                    │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ name          │ Lame                                                                                 │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ os            │ Linux                                                                                │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ ip            │ 10.10.10.3                                                                           │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ avatar        │ https://www.hackthebox.eu/storage/avatars/fb2d9f98400e3c802a0d7145e125c4ff.png       │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ avatar_thumb  │ https://www.hackthebox.eu/storage/avatars/fb2d9f98400e3c802a0d7145e125c4ff_thumb.png │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ points        │ 20                                                                                   │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ release       │ 2017-03-14 21:54:51                                                                  │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ retired_date  │ 2017-05-26 19:00:00                                                                  │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ maker         │ id: 1                                                                                │
# │               │ name: ch4p                                                                           │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ maker2        │                                                                                      │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ ratings_pro   │ 2331                                                                                 │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ ratings_sucks │ 220                                                                                  │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ user_blood    │ id: 22                                                                               │
# │               │ name: 0x1Nj3cT0R                                                                     │
# │               │ time: 18 days, 22 hours, 55 mins, 25 seconds                                         │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ root_blood    │ id: 22                                                                               │
# │               │ name: 0x1Nj3cT0R                                                                     │
# │               │ time: 18 days, 22 hours, 54 mins, 36 seconds                                         │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ user_owns     │ 9949                                                                                 │
# ├───────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
# │ root_owns     │ 10556                                                                                │
# ╘═══════════════╧══════════════════════════════════════════════════════════════════════════════════════╛


```


**Reset**

Of course you can also interact with the boxes. Here is how you request a reset of a box.

```bash
$ htb reset -h
# usage: htb reset [-h] BOX

# positional arguments:
#   BOX         The name of the box to reset. Resetting may take a few minutes
#               to take effect and may be cancelled by another user.

# optional arguments:
#   -h, --help  show this help message and exit

$ htb reset mango
# Attempting to reset Mango. This request often takes ~30 seconds, so be patient please...
# success: 1
# output: Mango will be reset in 2 minutes.
# used: 0
# of : 2 total resets
# total: 2

```


**Own**

You can submit flags with the own command. 

```bash
$ htb own -h
# usage: htb own [-h] -f FLAG -d [1-10] BOX

# positional arguments:
#   BOX                   The name of the box you want to own.

# optional arguments:
#   -h, --help            show this help message and exit
#   -f FLAG, --flag FLAG  The flag you want to submit to own the box. user/root
#                         is automatically determined by the server based on
#                         what flag you submit.
#   -d [1-10], --difficulty [1-10]
#                         The rating of how difficult you thought it was from
#                         1-10.


$ htb own --flag=abcdefghijklmnopqrstuvwxyz123456 --difficulty=5 heist
# Attempting to own Heist with flag: abcdefghijklmnopqrstuvwxyz123456 and rating: 5/9...
# Heist user is now owned.
# 1

```


VIP Only
---------

**Spawn**

You can interact with the new VIP interface's on demand launch capability with the spawn command.

```bash

$ htb spawn -h
# usage: htb spawn [-h] BOX

# positional arguments:
#   BOX         The name of the box to spawn. This will fail if you have another
#               box currently spawned. Terminate any spawned boxes and wait
#               until it actually shuts down before running this.

# optional arguments:
#   -h, --help  show this help message and exit

$ htb spawn chainsaw
# Attempting to spawn Chainsaw. This request often takes ~30 seconds, so be patient please...
# success: 1
# status: You have been assigned as an owner of this machine.

```

**Terminate**

And once youre done owning a box. Just terminate it and move on.

```bash
$ htb terminate -h
# usage: htb terminate [-h] BOX

# positional arguments:
#   BOX         The name of the box to terminate. Termination may take up to a
#               few minutes to take effect. Until then you will not be able to
#               spawn any new boxes.

# optional arguments:
#   -h, --help  show this help message and exit

$ htb terminate chainsaw
# Attempting to terminate Chainsaw. This request often takes ~30 seconds, so be patient please...
# success: 1
# status: Machine scheduled for termination.
```

Suggestions
------------------

If anyone has any feature requests, I will gladly hear them out but can't guarantee I will have time to implement them.

I'm @devx00 on HTB. And I am an admin of a Discord server dedicated to helping people get into InfoSec and (ethical) hacking in general. 
Feel free to message me at either, or on github.

Heres a link to the Discord server for anyone interested. [NullzSec Discord](https://discord.gg/TYw582m)