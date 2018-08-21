from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

Todo = {
    'todo1':'python work',
    'todo2':'assignments'
}


class Todo_task(Resource):
    

    def get(self):
        return Todo
    
    def post(self,todo_id):
        if todo_id not in Todo:
            parse = reqparse.RequestParser()
            parse.add_argument("task", type=str, help='add a task')
        

        if parse not in Todo:
            abort(404, message="no task is here!")

        return 'Success!'    

api.add_resource(Todo_task, '/')

if __name__ == "__main__":
    app.run(host='localhost',port='51210',debug=True) 
