import flask
from flask import Flask, render_template, request, jsonify
import mysql.connector

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="CebrayilDovletzade",
                               database="the_shop")
"""my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM products")
my_result = my_cursor.fetchall()"""

app = Flask(__name__, static_folder="/App/static", static_url_path="")


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
    my_result = my_cursor.fetchall()[0]
    return render_template("index.html", row=my_result, name=my_result[1], description=my_result[2],
                           price=my_result[3], picture=my_result[4])
    # return jsonify(my_result)


@app.route('/product/<pid>', methods=['GET'])
def product(pid):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM products")
    my_result = my_cursor.fetchone(pid)
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    mydb.close()
