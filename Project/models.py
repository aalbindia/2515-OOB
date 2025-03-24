from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, DECIMAL, ForeignKey, DateTime
from db import db
from datetime import datetime

#We dont use self because sqlaclchemy uses declarative mapping approach
#However, in SQLAlchemy, the attributes like id, name, price, etc., are class-level attributes that describe the table structure.
#They are not tied to a specific instance until an instance is created.

#When you create an instance of the class, SQLAlchemy automatically maps these class-level attributes to 
#instance-level attributes. 
#You would use self if you were defining methods that operate on instance data. 
#e.g. def outofstock(): return self.inventory == 0



#back_populates connects fields in both directions
class Category(db.Model):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")

class Customer(db.Model):
    __tablename__ = "customers"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String)
    orders = relationship("Order", back_populates="customer")
    
#Define all classes, that describe all entities in the program
class Product(db.Model):
    __tablename__ = 'products'
    id = mapped_column(Integer, primary_key=True)
    #our id is our primary key in the database, which uses integers
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10,2))
    inventory = mapped_column(Integer, default=0)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category",back_populates='products' )
    orders = relationship("Order", secondary="product_orders", back_populates="products")
    product_orders = relationship("ProductOrder", back_populates="product")

class Order(db.Model):
    __tablename__ = "Orders"

    id = mapped_column(Integer, primary_key=True)
    customer_id = mapped_column(Integer, ForeignKey("customers.id"), nullable=False)
    created = mapped_column(DateTime, nullable=False, default=db.func.now())
    completed = mapped_column(DateTime, nullable=True, default=None)
    amount = mapped_column(DECIMAL(6, 2), nullable=True, default=None)
    
    # Relationships
    customer = relationship("Customer", back_populates="orders")
    items = relationship('ProductOrder', back_populates='order')
    products = relationship("Product", secondary="product_orders", back_populates="orders")

#Our "Association" table to connect M-M relationship between Product and Order 
class ProductOrder(db.Model):
    __tablename__ = "Product Orders"

    # Composite primary key using both foreign keys
    product_id = mapped_column(ForeignKey("products.id"), primary_key=True)
    order_id = mapped_column(ForeignKey("orders.id"), primary_key=True)
    quantity = mapped_column(Integer, nullable=False)

    # Relationships
    product = relationship('Product', back_populates='product_orders')
    order = relationship('Order', back_populates='items')


