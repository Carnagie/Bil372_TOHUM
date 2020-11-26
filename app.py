from flask import Flask, render_template, url_for, redirect, request, session
#import psycopg2

app = Flask(__name__)
app.secret_key = "hello"
#con = psycopg2.connect(host="localhost", port="5432", database="tohum", user="postgres", password="147369")

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