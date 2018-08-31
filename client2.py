from requests import get,put
from app_server1 import Todo

# experimenting with function
#for i in Todo_review:

# Here is the automated command for client.py

def todo_prompt():
    """ making an automated command """

    for i in Todo:
        # msg = print(i) 
        var = "http://localhost:8000/{}".format(i)
        fetch = get(var).json()
        print(fetch)

todo_prompt()
