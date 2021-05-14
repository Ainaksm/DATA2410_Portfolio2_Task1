from flask import Flask, render_template, request, url_for, session, redirect
import mysql.connector
import pymysql
from mysql.connector.cursor import MySQLCursor

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="CebrayilDovletzade",
                               database="the_shop")

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/', methods=['GET'])
@app.route('/products', methods=['GET'])
def index():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM products")
    my_result = my_cursor.fetchall()
    return render_template("index.html", row=my_result)


@app.route('/product/<int:pid>', methods=['GET'])
def product(pid):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM products WHERE id = %d" % pid)
    my_result = my_cursor.fetchone()
    return render_template("products/prod.html", pid=pid, row=my_result)


@app.route('/product/<int:pid>', methods=['GET'])
def productToCart(pid):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT pName, description, price, picture FROM products WHERE id = %d" % pid)
    my_result = my_cursor.fetchone()
    return render_template("products/prod.html", pid=pid, row=my_result)


@app.route('/addtocart', methods=['POST', 'GET'])
def AddCart():
    Cursor = None
    try:

        product_id = int(request.form.get('product_id'))
        quantity = int(request.form.get('quantity'))
        my_cursor = mydb.cursor()
        product = my_cursor.query.filter_by(id=product_id).first()

        if product_id and quantity and request.method == "POST":

            # conn = mysql.connect()
            # cursor = conn.cursor(pymysql.cursors.DictCursor)
            # cursor.execute("SELECT * FROM products where id=%d" % product_id)
            # row = cursor.fetchone()

            # dictItem = {row['id']: {'name': row['pName'], 'description': row['description'], 'price': row['price'],
            # 'picture':row['picture'], 'quantity':quantity}}

            dictItem = {product_id: {'name': product.pName, 'description': product.description, 'price': product.price,
                                     'picture': product.picture, 'quantity': quantity}}

            dictItem = productToCart(product_id)
            if 'Shoppcart' in session:
                print(session['Shoppingcart'])


            else:
                session['Shoppingcart'] = dictItem
                return redirect(url_for('index'))

    except Exception as e:
        print(e)
        print("Test in except statement")

    finally:
        return redirect(request.referrer)


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
    mydb.close()
