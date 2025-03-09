
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Allows us to create a connection to the database

engine = create_engine('sqlite:///monday.db', echo=True)
#Relative path, that looks like an absolute path
#Database file always starts with /file.db

#Create a class sessiom, which connects to our db engine
Session = sessionmaker(bind=engine)

