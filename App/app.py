from flask import Flask, render_template, request, url_for, session, redirect
import mysql.connector
import pymysql

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


@app.route('/addcart', methods=['POST'])
def addCart():
    try:
        product_id = int(request.form.get('product_id', int))
        quantity = int(request.form.get('quantity', int))
        if product_id and quantity and request.method == "POST":
            dictItem = productToCart(product_id)
            if 'Shoppingcart' in session:
               print(session['Shoppingcart'])
               print("Test in if statement")

            else:
             session['Shoppincart'] = dictItem
             return redirect(request.referrer)
            print("Test in else statement")
    except Exception as e:
              print(e)
              print("Test in except statement")

    finally:
            return redirect(request.referrer)







if __name__ == '__main__':
    app.run(host="localhost", debug=True)
    mydb.close()



