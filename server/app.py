#!/usr/bin/env python3

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.debug = True
app.config["SECRET_KEY"] = "dev"
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)