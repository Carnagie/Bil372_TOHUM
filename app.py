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

@app.route('/fruits', methods=["POST","GET"])
def fruits():

    return render_template('fruits.html')

@app.route('/vegetables', methods=["POST","GET"])
def vegatables():

    return render_template('vegetables.html')

@app.route('/grains', methods=["POST","GET"])
def grains():

    return render_template('grains.html')

@app.route('/legumes', methods=["POST","GET"])
def legumes():

    return render_template('legumes.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page-404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('page-500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)