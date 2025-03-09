from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, DECIMAL



class Base(DeclarativeBase):
    pass

#Define all classes, that describe all entities in the program
class Product(Base):
    __tablename__ = 'products'
    id = mapped_column(Integer, primary_key=True)
    #our id is our primary key in the database, which uses integers
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10,2))
    inventory = mapped_column(Integer, default=0)
    category = mapped_column(String)


