import flask
from flask import Flask, render_template, request, jsonify, url_for
import mysql.connector

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="Melodi89",
                               database="the_shop")
"""my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM products")
my_result = my_cursor.fetchall()"""

app = Flask(__name__)

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
    # return jsonify(my_result)


@app.route('/product/<pid>', methods=['GET', 'POST'])
def product(pid):
    if request.method == "GET":
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM products")
        my_result = my_cursor.fetchmany()
        for row in my_result:
            return render_template("products/prod.html", pid=pid, row=row)

    # if request.method == "POST":
        # method for adding to cart


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    mydb.close()
