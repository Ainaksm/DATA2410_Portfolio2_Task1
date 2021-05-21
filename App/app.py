from flask import Flask, render_template, request, url_for, session, redirect
import mysql.connector

mydb = mysql.connector.connect(host="mysql1",
                               user="anonymous",
                               password="root",
                               database="the_shop")

app = Flask(__name__)
# secret key for session
app.config['SECRET_KEY'] = 'secretestsecret'


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

            session.modified = True
            if 'ShoppingCart' in session:
                session['ShoppingCart'] = merging_arrays(session['ShoppingCart'], product_array)

                print(session['ShoppingCart'])
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


@app.route('/cart')
def cart():
    # Redirecting to start-page if session not started or nothing is pur in the cart
    if 'ShoppingCart' not in session or len(session['ShoppingCart']) <= 0:
        return redirect(url_for('index'))

    total = 0
    # Calculating grand total
    for key, my_product in session['ShoppingCart'].items():
        total += int(my_product['price']) * int(my_product['quantity'])

    return render_template('products/cart.html', total=total)


@app.route('/remove-product/<int:pid>')
def remove_product(pid):
    # Redirecting to start-page if session not started or nothing is pur in the cart
    if 'ShoppingCart' not in session or len(session['ShoppingCart']) <= 0:
        return redirect(url_for('index'))

    try:
        session.modified = True
        for key, products in session['ShoppingCart'].items():
            if int(key) == pid:
                session['ShoppingCart'].pop(key, None)
                return redirect(url_for('cart'))
    except Exception as e:
        print(e)
        return redirect(url_for('cart'))


@app.route('/order')
def order():
    total = 0
    for key, my_product in session['ShoppingCart'].items():
        discount = 100
        total += int(my_product['price']) * int(my_product['quantity'])
        amountToPay = total - total * (discount / 100)

    return render_template('products/order.html', total=total, amountToPay=amountToPay, discount=discount)


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
    app.run(host="0.0.0.0", debug=True)
    mydb.close()
