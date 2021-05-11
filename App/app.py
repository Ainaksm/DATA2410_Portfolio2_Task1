from flask import Flask, render_template, request, url_for, session, redirect
import mysql.connector

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="root",
                               database="the_shop")

app = Flask(__name__)


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
