# we are going to build an API, or a web service, for a todo app.
# The API service will be implemented using a REST-based architecture

# Create an item in the todo list
# Read the complete todo list
# Update the items with status as "Not Started", "In Progress", or "Complete"
# Delete the items from the list
# https://stackabuse.com/building-a-todo-app-with-flask-in-python/
# pip install Flask

# Day 3 : Learned to create Hello world message using flask to display

from flask import Flask, request, Response
import json
from helpClass import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello-world!\n'


# Day 4 : import modules and set up some route

@app.route('/item/new', methods=['POST'])
def add_item():
    req_data = request.get_json()
    item = req_data['item']

    res_data = helper.add_to_list(item)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response
