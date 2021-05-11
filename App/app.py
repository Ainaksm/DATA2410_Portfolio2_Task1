import flask
from flask import Flask, render_template, request, jsonify, url_for, session, redirect, flash
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


@app.route('/product/<int:pid>', methods=['GET'])
def product(pid):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM products WHERE id = %d" % pid)
    my_result = my_cursor.fetchone()
    return render_template("products/prod.html", pid=pid, row=my_result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    mydb.close()
