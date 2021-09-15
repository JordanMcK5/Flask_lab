from app import app
from flask import render_template
from models.order_list import orders

@app.route("/orders")
def index():
    return render_template("index.html", title = "orders", orders=orders)

@app.route("/order/<index>")
def order(index):
    return render_template("order.html",title = "single-order", order=orders[int(index)])
