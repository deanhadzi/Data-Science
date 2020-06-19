from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pickle import load
# from model import model
# from strain info import strain info

load_dotenv()

'''Configuration of app'''
def create_app():
    app = FLask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI']  = config('SQLALCHEMY_URI')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

'''Initaialise Database'''
db = SQLAlchemy(app)

'''temp data (TODO)'''

'''temp model (TODO)'''

'''Home page'''
@app.route("/")
def home:
    '''Root Page'''

    Returns:
        #TODO
    
    return render_template('home.html')

@app.route("/request/", methods = ['GET', 'POST'])
def search(user_input=None):
    '''Input from user and gives something back (TODO)'''

return app