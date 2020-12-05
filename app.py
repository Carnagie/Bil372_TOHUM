from flask import Flask, render_template, url_for, redirect, request, session
import psycopg2

app = Flask(__name__)
app.secret_key = "hello"

"""
secure database useage pattern (DO NOT USE 1 CONNECTION FOR MORE THAN ONE EXECUTION)
con = psycopg2.connect(host="localhost", port="9999", database="tohum", user="super", password="whqrnr&6mxAj7")
cur = con.cursor()
cur.execute(<your sql string>)
cur.commit()

//optional if you try to get table data
cur.fetchall()

cur.close()
con.close()
"""

@app.route('/')
def homepage():
    return "deneme"

@app.route('/login',methods=["POST","GET"])
def login():
    pass

@app.route('/register', methods=["POST","GET"])
def register():
    pass

if __name__ == '__main__':
    app.run(debug=True)