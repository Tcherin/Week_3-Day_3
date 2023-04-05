from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template("bookshop.html", title="Home", orders=orders)

@app.route("/<int:id>")
def single_task(id):
    return render_template("order.html", title="order1", order=orders[id-1])