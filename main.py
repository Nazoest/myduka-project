from flask import Flask, redirect,render_template, request, url_for
from database import fetch_data, insert_products,insert_sales,insert_stock

#instance of flask class
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def prods():
    products=fetch_data('products')
    return render_template('products.html',myproducts=products)

@app.route('/add_products',methods=['GET',"POST"])
def add_products():
    if request.method=='POST':
        pname=request.form['product_name']
        bp=request.form["buying_price"]
        sp=request.form["selling_price"]
        print(pname,sp,bp)
        new_product = (pname,bp, sp)
        insert_products(new_product)

    return redirect(url_for('prods'))

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method=='POST':
        pid=request.form['pid']
        quantity=request.form["quantity"]
        new_sale = (pid,quantity)
        print(new_sale)
        insert_sales(new_sale)

    return redirect(url_for('sales'))

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        pid=request.form['pid']
        quantity=request.form["stock_quantity"]
        new_stock = (pid,quantity)
        insert_stock(new_stock)

    return redirect(url_for('stock'))


@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    products=fetch_data('products')
    return render_template('sales.html',sales=sales,products=products)

@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    products=fetch_data('products')
    return render_template('stock.html',stock=stock,products=products)

app.run(debug=True)