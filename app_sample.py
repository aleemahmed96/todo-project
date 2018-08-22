from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

Todo = {
    'todo1':'python work',
    'todo2':'assignments'
}


class Todo_task(Resource):


    def get(self):
        return Todo

    def put(self,todo):

# creating request.form
        Todo[todo] = request.form['data']


        if todo not in Todo:
            abort(404, message="no task is here!")
        else:
            abort(404,message="task is already added!")


        print ('Success!')
        return {todo : Todo[todo]}


api.add_resource(Todo_task, '/<string:todo>')

if __name__ == "__main__":
    app.run(host='localhost',port='8000',debug=True)
