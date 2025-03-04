import csv
import sys
from models import Product, Customer, Category, Base
from db import Session, engine
from sqlalchemy import select

session = Session()
def import_products():
     with open("products.csv", 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                #check if category already exists
                category_name = item['category']
                category = session.execute(select(Category).where(Category.name == category_name)).scalar()
                if not category:
                     #create new category if doesnt exist
                     category = Category(name=category_name)
                     session.add(category)
                     session.commit()
                #Create product and associate it with the category
                products = Product(name = item["name"], 
                    price = float(item["price"]), 
                    inventory=int(item["available"]), 
                    category=category
                ) #Stores product in product class and in our initialized variable
                session.add(products)
            session.commit()
            print("Products imported")

def create_table():
     Base.metadata.create_all(bind=engine)
     print('Tables created')
def drop_table():
     Base.metadata.drop_all(bind=engine)

def import_customers():
     with open('customers.csv', 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
               customer = Customer(name = row["name"], 
                    phone = row["phone"]
                )
               session.add(customer)
          session.commit()
          print('Customer imported')

def query_products():
     statement = select(Product).where(Product.id < 5)
     results = session.execute(statement)
     for prod in results.scalars():
          print(f'Product: {prod.name}, Price: {prod.price}, Inventory: {prod.inventory}, Category: {prod.category} ')

def query_customers():
     statement = select(Customer)
     results = session.execute(statement)
     for cus in results.scalars():
          print(f'Name: {cus.name}, Phone: {cus.phone}')

if __name__ == "__main__":
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
    else:
         print('Invalid argument')

    
    
                 
     
