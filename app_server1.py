from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

Todo = {
    'todo1':'python work',
    'todo2':'assignments'
}


class Todo_review(Resource):
	""" to see the contents of task in index page """

	def get(self):
		""" showing all tasks """
		return Todo

class Todo_task(Resource):
    """ to add tasks and show them individually """

    def get(self,todo):
        """ showing specific tasks """

        if todo not in Todo:
            abort(404, message="no task is here!")

        return Todo[todo]


    def put(self,todo):
        """ updating tasks """
# creating request.form
        Todo[todo] = request.form['data']

        if todo not in Todo:
            abort(404, message="no task is here!")
        else:
            abort(404,message="task is already added!")



    def post(self,todo):
        """ adding a new task """
        Todo[todo] = request.form['data']


        print ('Success!')
        return {todo : Todo[todo]}


api.add_resource(Todo_task, '/<string:todo>')
api.add_resource(Todo_review, '/')

if __name__ == "__main__":
    app.run(host='localhost',port='8000',debug=True)
