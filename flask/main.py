from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def welcome():
    print("my first server")
    return "welcome to server with flash"


@app.route("/users", methods=['GET'])
def users():
    return "list all the users"


@app.route("/user", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    if request.method == 'POST':
        return "create user"
    elif request.method == 'PUT':
        return "update user"
    elif request.method == 'DELETE':
        return "delete user"
    else:
        return "get user"
