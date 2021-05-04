from flask import Flask, render_template, request
import mysql.connector

# remember to adjust
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="Melodi89",
                               database="the_shop")
my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM products")
my_result = my_cursor.fetchall()

app = Flask(__name__)


@app.route('/')
def index():
    my_cur = mydb.cursor()
    my_cur.execute("SELECT * FROM products")
    my_res = my_cur.fetchall()
    return render_template("index.html", data=my_res)


@app.route('/product/<pid>', methods=['GET'])
def product(pid):
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    mydb.close()
