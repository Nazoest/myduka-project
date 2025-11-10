from functools import wraps
from flask import Flask, redirect,render_template, request, session, url_for,flash
from flask_bcrypt import Bcrypt
from database import fetch_data, get_profit_per_day, get_profit_per_product, get_sales_per_day, get_sales_per_product, insert_products,insert_sales,insert_stock,insert_user,check_email, update_product

#instance of flask class
app=Flask(__name__)
app.secret_key='sdfgyhui'
bcrypt=Bcrypt(app)

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/products')
@login_required
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

@app.route('/edit_product',methods=['GET',"POST"])
def edit_product():
    if request.method=='POST':
        pid=request.form['product_id']
        pname=request.form['product_name']
        bp=request.form["buying_price"]
        sp=request.form["selling_price"]
        new_product = (pname,bp, sp,pid)
        update_product(new_product)

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

@app.route('/dashboard')
@login_required
def dashboard():
    sales_per_product=get_sales_per_product()
    profit_per_product=get_profit_per_product()
    sales_per_day=get_sales_per_day()
    profit_per_day=get_profit_per_day()
    product_names=[]
    product_profits=[]
    for i in profit_per_product:
        product_names.append(i[1])
        product_profits.append(float(i[2]))

    psale_names=[]
    product_sales=[]
    for i in sales_per_product:
        psale_names.append(i[1])
        product_sales.append(float(i[2]))

    dates=[]
    dsales=[]

    for i in sales_per_day:
        dates.append(str(i[0]))
        dsales.append(float(i[1]))

    pdates=[]
    dprofits=[]
    for i in profit_per_day:
        pdates.append(str(i[0]))
        dprofits.append(float(i[1]))

    return render_template('dashboard.html',product_profits=product_profits,product_names=product_names,sales_names=psale_names,product_sales=product_sales,sale_names=psale_names,dates=dates,dsales=dsales,pdates=pdates,dprofits=dprofits)

@app.route('/sales')
@login_required
def sales():
    sales=fetch_data('sales')
    products=fetch_data('products')
    return render_template('sales.html',sales=sales,products=products)

@app.route('/stock')
@login_required
def stock():
    stock=fetch_data('stock')
    products=fetch_data('products')
    return render_template('stock.html',stock=stock,products=products)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        user=check_email(email)
        if user==None:
            print("Email not found. Please register first.")
            return redirect(url_for('register'))        
        else:
            if bcrypt.check_password_hash(user[3],password):
                session['email']=email
                flash("Login Successful","success")
                return redirect(url_for('dashboard'))
            else:
                return "Incorrect password. Please try again."
            
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        fname=request.form['name']
        email=request.form['email']
        password=request.form['password']
        existing_user=check_email(email)
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        if existing_user:
            return "Email already exists. Please login or use different email."
        new_user=(fname,email,hashed_password)
        print(new_user)
        insert_user(new_user)
        print("User registered successfully.")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("You have been logged out.","info")
    return redirect(url_for('login'))

app.run(debug=True)