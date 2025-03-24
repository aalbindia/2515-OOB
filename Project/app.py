from flask import Flask,render_template
from pathlib import Path
from db import db
from models import Customer, Category, Product, Order, ProductOrder


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/products")
def products():
    statement = db.select(Product)
    result = db.session.execute(statement).scalars().all()
    return render_template("products.html", data=result)

@app.route("/categories")
def category():
    statement = db.select(Category)
    result = db.session.execute(statement).scalars().all()
    return render_template("categories.html", data=result)

@app.route("/customers")
def customer():
    statement = db.select(Customer)
    result = db.session.execute(statement).scalars().all()
    return render_template("customer.html", data=result)

@app.route("/categories/<string:name>")
def category_detail(name):
    category = db.session.execute(db.select(Category).where(Category.name == name)).scalar()
    if category:
        products = db.session.execute(db.select(Product).where(Product.category_id == category.id)).scalars().all()
        return render_template("category_detail.html", category=category, products=products)
    else:
        return "Category Not Found", 404
    

@app.route("/customers/<int:id>") #Access by /customers/1 (shows customer 1)
def customer_detail(id):
    customer = db.session.execute(db.select(Customer).where(Customer.id == id)).scalar() #Since ids are unique use .scalar to return single object, as there is only one
    print(f'customer: {customer}')
    if customer:
        return render_template("customer_detail.html", customer=customer)
    else:
        return "Customer Not found" , 404

@app.route("/orders")
def orders():
    order = db.session.execute(db.select(Order)).scalars().all()
    if order:
        return render_template("orders.html", orders=order)
    else:
        return "No Orders Found", 404
    
@app.route("/orders/<int:ORDER_ID>")
def order_detail(ORDER_ID):
    order = db.session.execute(db.select(Order).where(Order.id == ORDER_ID)).scalar()
    if order:
        total_amount = sum(item.product.price * item.quantity for item in order.items)
        return render_template("order_detail.html", order=order, total=total_amount)
    else:
        return "Order details Unknown", 404

if __name__ == "__main__":
    app.run(debug=True,port=8080)
   