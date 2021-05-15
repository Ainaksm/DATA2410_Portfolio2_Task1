import flask
from flask import Flask, render_template, request, jsonify, url_for, session, redirect, flash
import mysql.connector

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="CebrayilDovletzade",
                               database="the_shop")
"""my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM products")
my_result = my_cursor.fetchall()"""

app = Flask(__name__)
# secret key for session
app.config['SECRET_KEY'] = 'secretestsecret'

""""@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def serve_page(path):
    print("Request received for {}".format(path))
    return flask.send_from_directory('/App/static', path)"""


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


@app.route('/add-to-cart', methods=["POST"])
def add_to_cart():
    try:
        product_id = request.form.get('product_id')

        qty = request.form.get('quantity')

        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM products WHERE id = %s" % product_id)
        my_product = my_cursor.fetchone()

        if product_id and qty and request.method == "POST":
            product_array = {product_id: {'name': my_product[1], 'price': my_product[3], 'quantity': qty}}

            if 'ShoppingCart' in session:
                print(session['ShoppingCart'])

                if product_id in session['ShoppingCart']:
                    print("Product already in cart")
                else:
                    session['ShoppingCart'] = merging_arrays(session['ShoppingCart'], product_array)
                    # Redirecting to same page
                    return redirect(request.referrer)

            else:
                session['ShoppingCart'] = product_array
                # Redirecting to same page
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        # Redirecting to same page
        return redirect(request.referrer)


def merging_arrays(array, other_array):
    if isinstance(array, list) and isinstance(other_array, list):
        return array + other_array
    elif isinstance(array, dict) and isinstance(other_array, dict):
        return dict(list(array.items()) + list(other_array.items()))
    elif isinstance(array, set) and isinstance(other_array, set):
        return array.union(other_array)
    else:
        return False



if __name__ == '__main__':
    app.run(host="localhost", debug=True)
    mydb.close()
