import csv
import operator
class Product:
    def __init__(self, name, price, inventory, category):
        self.name = name
        self.price = price
        self.inventory = inventory
        self.category = category
    def __repr__(self): #__repre__ class returns strings of objects and are ,mainly used for development and debugging
        return f"Product(name='{self.name}', price={self.price}, inventory={self.inventory}, category='{self.category}')"

class ProductManager:
    def __init__(self, filename = 'products.csv'):
        self.product = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for product in reader:
                products = Product(product["name"], product["price"], product["available"], product["category"]) #Stores product in product class and in our initialized variable
                self.product.append(products)
    
    def find_byname(self,text): 
        product = [product for product in self.product if product.name == text]
        return product
    
    def get_products(self,order_by, reverse = False):
        return sorted(self.product, key= operator.attrgetter(order_by), reverse=reverse)
            #operator.attrgetter() returns a function that retrieves the specified attribute from that object specified in the argument(accepts a string or tuple of strings)
            #Retrieves attribute of the Product objects based on the string order_by
    def get_products_in(self,category):
        return [product for product in self.product if product.category == category]

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __repr__(self): #__repre__ class returns strings of objects and are ,mainly used for development and debugging
        return f"Customer Information: {self.name}, {self.phone}"

class CustomerManager:
    def __init__(self):
        self.customers = []
        try:
            with open('customers.csv', 'r') as file:
                reader = csv.DictReader(file)
                for info in reader:
                    cus_info = Customer(info["name"], info["phone"])
                    self.customers.append(cus_info)
        except FileNotFoundError:
            print('Error: File not found')
        except KeyError:
            print('Error: File must have name and phone column')

    def return_name(self, name):
        match_customer = [customer for customer in self.customers if customer.name == name]
        return match_customer if match_customer else []
    
    def return_phone(self, phone):
        for customer in self.customers:
            if customer.phone == phone:
                return customer
        return None
    
#If you want it to return none instead of empty list: [product if product.category == category else None for product in self.product]
d = ProductManager()
print(d.get_products("price", reverse=True))
print(d.get_products_in('dair'))
cus = Customer('Allen', 7787141865)
print(cus)
manager = CustomerManager()
# for customer in manager.info:
#         print(customer)

print(manager.return_name('Deanna Ross'))
print(manager.return_phone(''))
