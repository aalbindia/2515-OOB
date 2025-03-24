

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

#Allows us to create a connection to the database


#Relative path, that looks like an absolute path
#Database file always starts with /file.db

#Create a class sessiom, which connects to our db engine

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
#Creates db object which we can use for all tasks requiring the db(e.g. defining models, querying)
#Object has the base class registered for ORM-related features