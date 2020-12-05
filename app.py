from flask import Flask, render_template, url_for, redirect, request, session
#import psycopg2

app = Flask(__name__)
app.secret_key = "hello"
#con = psycopg2.connect(host="localhost", port="5432", database="tohum", user="postgres", password="147369")





@app.route('/', methods=["GET","POST"])
def index():

    return render_template('index.html')



@app.route('/login',methods=["POST","GET"])
def login():

    return render_template('login.html')

@app.route('/register', methods=["POST","GET"])
def register():
    

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)