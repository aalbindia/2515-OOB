import csv
import random
import sys
from models import Product, Customer, Category, Order, ProductOrder
from db import db
from sqlalchemy import select, func
from app import app
session = db.session

#Function that handles category and products table
def import_products():
     with open("/csv/products.csv", 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                #check if category already exists
                category_name = item['category']
                category = session.execute(select(Category).where(Category.name == category_name)).scalar()
                if not category:
                     #create new category if doesnt exist
                     category = Category(name=category_name)
                     db.session.add(category)
                     db.session.commit()
                #Create product and associate it with the category
                products = Product(name = item["name"], 
                    price = float(item["price"]), 
                    inventory=int(item["available"]), 
                    category=category
                ) #Stores product in product class and in our initialized variable
                db.session.add(products)
            db.session.commit()
            print("Products imported")
            
#create and drop table
def create_table():
     db.create_all()
     print('Tables created')
def drop_table():
     db.drop_all()

#handles Customer table
def import_customers():
     with open('/csv/customers.csv', 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
               customer = Customer(name = row["name"], 
                    phone = row["phone"]
                )
               db.session.add(customer)
          db.session.commit()
          print('Customer imported')

#basic query functions, that displays products and customer table
def query_products():
     statement = select(Product).where(Product.id < 5)
     results = db.session.execute(statement)
     for prod in results.scalars():
          print(f'Product: {prod.name}, Price: {prod.price}, Inventory: {prod.inventory}, Category: {prod.category} ')

def query_customers():
     statement = select(Customer)
     results = db.session.execute(statement)
     for cus in results.scalars():
          print(f'Name: {cus.name}, Phone: {cus.phone}')

def create_random_orders(num_orders=5):
    """
    Creates random orders with random products and quantities.
    
    Args:
        num_orders (int): Number of orders to create. Defaults to 5.
    """
    for _ in range(num_orders):
        # Get a random customer
        random_customer = db.session.execute(
            select(Customer).order_by(func.random())
        ).scalar()
        
        if not random_customer:
            print("No customers found in database")
            return
        
        # Create a new order for this customer
        new_order = Order(customer=random_customer)
        db.session.add(new_order)
        
        # Get a random number of products (between 2 and 5)
        num_products = random.randint(2, 5)
        random_products = db.session.execute(
            select(Product).order_by(func.random()).limit(num_products)
        ).scalars()
        
        # Add products to the order with random quantities
        for product in random_products:
            quantity = random.randint(1, 10)  # Random quantity between 1 and 10
            product_order = ProductOrder(
                product=product,
                order=new_order,
                quantity=quantity
            )
            db.session.add(product_order)
    
    # Commit all changes
    try:
        db.session.commit()
        print(f"Successfully created {num_orders} random orders")
    except Exception as e:
        db.session.rollback()
        print(f"Error creating orders: {str(e)}")

if __name__ == "__main__":
    with app.app_context():
         
     if len(sys.argv) < 2:
          print('Invalid usage, e.g. create, drop, import, query')
          sys.exit(1)
     
     command = sys.argv[1]
     if command == "create":
          create_table()
     elif command == "drop":
          drop_table()
     elif command == "import":
          import_products()
          import_customers()
     elif command == "query":
          query_customers()
          query_products()
     elif command == "random_orders":
          create_random_orders()
     else:
          print('Invalid argument')

    
    
                 
     
