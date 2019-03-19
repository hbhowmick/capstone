# importing Flask class from flask.py file
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# creating an instance of the Flask class, in order to run this application
# name parameter will default to folder name
app = Flask(__name__)


# create other variable instances
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# from the app folder, import the routes.py file, and startup at the index route
from app import routes
