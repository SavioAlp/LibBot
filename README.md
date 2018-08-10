# LibBot
An script to automatically reserve a study room in the UVIC Library.

### Motivation
1. Crowded and Overpopulated
.. UVIC is very crowded during the school year and is incredibly difficult to find a place to 
.. find a place to study for long periods of time. 
2. Laziness
.. Too lazy to book a room everyday.

### How it works.
The python script reads off a `json` file that contains netlink IDs and passwords. Multiple
IDs are needed because UVIC Libraries only allows to book 2 hours per day/ per user. To book 
a room for a full day, you would need 7 IDs. 

The script books 7 days in advance (UVIC's maximum booking time) everyday at midnight and secures
_n_ number of spots, where _n_ is the number of netlink ids. The script also takes into account 
the reserved spots UVIC Library has on 7 day reservations.

The script does a simple `POST` command with the required fields to send. (day, time room.. etc)


### Improvement
1. Fill up reserved gaps once released-- Usually within 1-2 days
2. Dynamically located JSON file -- Currently statically assigned.

### How to use
⋅⋅* Python 3
⋅⋅* JSON File named _"netlinkIDs.json"_ with two fields called `"usernames"` and `"passwords"`
⋅⋅⋅ with usernames and passwords in an array.
