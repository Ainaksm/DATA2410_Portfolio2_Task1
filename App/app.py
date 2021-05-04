from flask import Flask, render_template, request
import mysql.connector

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
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
