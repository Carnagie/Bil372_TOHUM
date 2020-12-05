from flask import Flask, render_template, url_for, redirect, request, session, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "hello"
con = psycopg2.connect(host="localhost", port="9999", database="tohum", user="super", password="whqrnr&6mxAj7")




@app.route('/', methods=["GET","POST"])
def index():

    return render_template('index.html')



@app.route('/login',methods=["POST","GET"])
def login():

    return render_template('login.html')

@app.route('/register', methods=["POST","GET"])
def register():

    if request.method == "POST":
        email = request.form["email"]
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        country = request.form["country"]
        region = request.form["region"]
        city = request.form["city"]
        district = request.form["district"]
        first_password = request.form["first_password"]
        second_password = request.form["second_password"]

        cur = con.cursor()
        cur.execute("select * from ciftci where ciftcimail='{}'".format(email))
        ret = cur.fetchall()
        if ret or first_password != second_password:
            print("hata mesaji")
            return redirect(url_for("register"))
        else:
            print("kaydolabilir")
            cur.execute("insert into ciftci (ciftcifname, ciftcilname, ciftcimail, ciftcipassword) values(%s, %s, %s, %s)", (first_name,last_name, email, first_password))
            cur.execute("select ciftciid from ciftci where ciftcimail='{}'".format(email))
            ciftciID = cur.fetchone()[0]
            con.commit()
            #cur.execute("select ilceid from ")
            print(ciftciID)
            #TODO @carnagie insert to ilce bolge...
        cur.close()

        return redirect(url_for("register"))

    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)










































