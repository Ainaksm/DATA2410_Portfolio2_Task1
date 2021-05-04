from flask import Flask, render_template, request
import mysql.connector

# from sqlalchemy.dialects import mysql
"""mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="root",
                               database="the_shop")
my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM the_shop")
my_result = my_cursor.fetchall()"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
