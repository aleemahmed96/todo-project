from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

Todo = {}


class Todo_task(Resource):
    

    def get(self,todo_id,task):
        return Todo[todo_id] == str(task)
    
    def post(self,todo_id):
        if todo_id not in Todo:
            parse = reqparse.RequestParser()
            parse.add_argument("task", type=str, help='add a task')
        

        if parse not in Todo:
            abort(404, message="no task is here!")

        return 'Success!'    

api.add_resource(Todo_task, '/<string:todo_id>')

if __name__ == "__main__":
    app.run(host='localhost',port='51210',debug=True) 
