from flask import Flask, render_template, url_for, redirect, request, session, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "hello"
con = psycopg2.connect(host="localhost", port="9999", database="tohumdb", user="super", password="whqrnr&6mxAj7")


@app.route('/', methods=["GET","POST"])
def index():
    if "admin" in session or "user" in session:
        return render_template('index.html',data="T")
    else:
        return render_template('index.html',data="F")

@app.route('/admin',methods=["POST","GET"])
def admin():
    if "admin" not in session:
        return redirect(url_for("login"))
    else:
        return "admin sayfasi"

@app.route('/user', methods=["POST","GET"])
def user():
    if "user" in session:
        user = session["user"]
        return "user sayfasi"
    else:
        return redirect(url_for("login"))

@app.route('/login',methods=["POST","GET"])
def login():

    if "admin" in session:
        return redirect(url_for("admin"))

    elif "user" in session:
        return redirect(url_for("user"))

    else:
        if request.method == "POST":

            cur = con.cursor()
            email = request.form["email"]
            password = request.form["password"]
            cur.execute("select ciftcipassword from ciftci where ciftcimail='{}'".format(email))
            truePassword = cur.fetchone()
            con.commit()
            cur.close()

            if email == "admin@admin.com" and password == "admin":
                session["admin"] = "admin"
                return redirect(url_for("admin"))

            if truePassword == None:
                return redirect(url_for("login"))

            else:
                if password == truePassword[0].__str__():
                    session["user"] = "user"
                    return redirect(url_for("user"))
                else:
                    return redirect(url_for("login"))



        else:
            if "user" in session:
                return redirect(url_for("user"))
            return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("admin", None)
    session.pop("user", None)
    return redirect(url_for("login"))

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

@app.route('/fruits', methods=["POST","GET"])
def fruits():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            name = request.form["name"]
            region = request.form["region"]
            opposite = request.form["opposite"]
            year = request.form["year"]
            area = request.form["area"]
            coefficient = request.form["coefficient"]
            ton = request.form["ton"]
            cur = con.cursor()
            if name == None and region == None and opposite == None and year == None and area == None and coefficient == None and ton == None:
                cur.execute("select * from product where type=1")
            elif name:
                cur.execute("select * from product where type=1 and name='{}'".format(name))
            elif region:
                cur.execute("select * from product where type=1 and regionid=(select regionid from region where regionname='{}')".format(region))
            #elif opposite:
            #    cur.execute("select * from product where type=1 and name='{}'".format(opposite))
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()
            return redirect(url_for("fruits"))

        else:
            return render_template('fruits.html')

@app.route('/vegetables', methods=["POST","GET"])
def vegatables():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        return render_template('vegetables.html')

@app.route('/grains', methods=["POST","GET"])
def grains():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        return render_template('grains.html')

@app.route('/legumes', methods=["POST","GET"])
def legumes():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
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










































