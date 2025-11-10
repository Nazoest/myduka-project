#import the psycopg2 library
import psycopg2

conn=psycopg2.connect(host='localhost',port='5432',user="postgres",password='Nazo',dbname='myduka_db')

curr=conn.cursor()
#print(data)

""" def fetch_products():
    curr.execute("SELECT * FROM PRODUCTS;")
    prods=curr.fetchall()
    return prods
 """
def insert_products(values):
    query="insert into products(name, buying_price, selling_price)values(%s,%s,%s);"
    curr.execute(query,values)
    conn.commit()

def update_product(values):
    query = "UPDATE products SET name = %s, buying_price = %s, selling_price = %s WHERE id = %s;"
    curr.execute(query, values)
    conn.commit()

#new_product=('maize',120,150)
#insert_products(new_product)

def insert_sales(values):
    query="insert into sales(pid,quantity,created_at)values(%s,%s,now());"
    curr.execute(query,values)
    conn.commit()

new_sale=(1,45)
#insert_sales(new_sale)

def check_email(email):
    query="select * from users where email=%s;"
    curr.execute(query,(email,))
    user=curr.fetchone()
    return user

def insert_stock(values):
    query="insert into stock(pid,stock_quantity,created_at)values(%s,%s,now());"
    curr.execute(query,values)
    conn.commit()

new_stock=(1,12)
#insert_stock(new_stock)

def get_sales_per_day():
    query="SELECT DATE(s.created_at) AS sale_date,SUM(p.selling_price * s.quantity) AS total_sales FROM sales as s JOIN products as p ON s.pid = p.id GROUP BY DATE(s.created_at) ORDER BY sale_date;"
    curr.execute(query)
    sales_per_day=curr.fetchall()
    return sales_per_day


def get_profit_per_day():
    query="SELECT DATE(s.created_at) AS sale_date,SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit FROM sales as s JOIN products as p ON s.pid = p.id GROUP BY DATE(s.created_at) ORDER BY sale_date;"
    curr.execute(query)
    profit_per_day=curr.fetchall()
    return profit_per_day


def get_profit_per_product():
    query="SELECT p.id AS product_id,p.name AS product_name,SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit FROM sales s JOIN products p ON s.pid = p.id GROUP BY p.id, p.name;"
    curr.execute(query)
    profit=curr.fetchall()
    return profit

#profits=get_profit_per_product()
#print(profits)
def get_sales_per_product():
    query="SELECT p.id AS product_id,p.name AS product_name, SUM(p.selling_price * s.quantity) AS total_sales FROM sales s JOIN products p ON s.pid = p.id GROUP BY p.id, p.name ORDER BY total_sales DESC;"
    curr.execute(query)
    sales_per_product=curr.fetchall()
    return sales_per_product

#sales=get_sales_per_product()
#print(sales)


""" def get_sales():
    curr.execute("select * from sales")
    sales=curr.fetchall()
    return sales
 """

def fetch_data(table_name):
    query=f"select * from {table_name}"
    curr.execute(query)
    data=curr.fetchall()
    return data
#sales=fetch_data("sales")
#products=fetch_data("products")
#stock=fetch_data("stock")
#print(products)
#print(stock)
#print(sales)



def insert_stock(values):
    curr.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()


def get_profit_per_product():
    curr.execute("SELECT p.id AS product_id,p.name AS product_name,SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit FROM sales s JOIN products p ON s.pid = p.id GROUP BY p.id, p.name ORDER BY total_profit DESC;")
    profit_per_product=curr.fetchall()
    return profit_per_product

def get_sales_per_product():
    query="SELECT p.id AS product_id,p.name AS product_name, SUM(p.selling_price * s.quantity) AS total_sales FROM sales s JOIN products p ON s.pid = p.id GROUP BY p.id, p.name ORDER BY total_sales DESC;"
    curr.execute(query)
    sales_per_product=curr.fetchall()
    return sales_per_product

def insert_user(user_details) : 
    query="insert into users(full_name, email, password) values(%s,%s,%s)"
    curr.execute(query,user_details) 
    conn.commit()
