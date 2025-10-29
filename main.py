from flask import Flask, redirect,render_template, request, url_for
from database import fetch_data, insert_products

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