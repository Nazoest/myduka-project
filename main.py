from flask import Flask,render_template
from database import fetch_data

#instance of flask class
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def prods():
    products=fetch_data('products')
    print(products)
    return render_template('product.html',myproducts=products)

@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    print(sales)
    return render_template('sales.html',sales=sales)

@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    print(stock)
    return render_template('stock.html',stock=stock)

app.run(debug=True)