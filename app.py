# import flask dependencies

from flask import Flask

# create a new app instance

app = Flask(__name__)



# first, define the starting point, known as the ROOT,  this line of code is the root = @app.route('/')

@app.route('/')

def hello_world():
    
    return 'Hello world'


