from requests import get,put

## in order to add new task

put('http://localhost:8000/todo4',data={'data': 'Remember the milk'}).json()

# in order to get requests

msg = get("http://localhost:8000").json()
print(msg)

# as two tasks are in the server
todo1 = get("http://localhost:8000/todo1").json()
print(todo1)
todo2 = get("http://localhost:8000/todo2").json()
print(todo2)

# the third task is not available, therefore
# it will show message regarding "no task is here!"

todo3 = get("http://localhost:8000/todo3").json()
print(todo3)

# in order to overwrite these tasks you
# can use the same command in line 5, but
# changes are there regarding app_server files
# be sure to check them out.

# app_server1.py will overwrite easily
# app_server2.py will not overwrite easily

# future enhancements will be given to
# administrator for overriding tasks if
# todo lists is made in collaboration with team
