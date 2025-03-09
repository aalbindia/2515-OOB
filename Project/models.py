from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String, DECIMAL, ForeignKey

#We dont use self because sqlaclchemy uses declarative mapping approach
#However, in SQLAlchemy, the attributes like id, name, price, etc., are class-level attributes that describe the table structure.
#They are not tied to a specific instance until an instance is created.

#When you create an instance of the class, SQLAlchemy automatically maps these class-level attributes to 
#instance-level attributes. 
#You would use self if you were defining methods that operate on instance data. 
#e.g. def outofstock(): return self.inventory == 0

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
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category",back_populates='products' )

#back_populates connects fields in both directions
class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")

class Customer(Base):
    __tablename__ = "customers"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String)


