from flask import Flask, render_template, url_for, redirect, request, session, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "hello"
#con = psycopg2.connect(host="localhost", port="9999", database="tohumdb", user="super", password="whqrnr&6mxAj7")
con = psycopg2.connect(host="localhost", port="5432", database="tohumdb", user="postgres", password="facethest0rm")

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
            cur.execute("select password from tohumschema.farmer where mail='{}'".format(email))
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

    cur = con.cursor()
    cur.execute("SELECT * FROM tohumschema.city;")
    cities = cur.fetchall()
    cur.close()


    if request.method == "POST":

        email = request.form["email"]
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        country = request.form["country"]
        region = request.form["region"]
        city = request.form["city"]
        for i in cities:
            if city == i[2]:
                city = i[1]
                break
        first_password = request.form["first_password"]
        second_password = request.form["second_password"]

        cur = con.cursor()
        cur.execute("select * from tohumschema.farmer where mail='{}'".format(email))
        ret = cur.fetchall()
        if ret or first_password != second_password:
            print("hata mesaji")
            return redirect(url_for("register"))
        else:
            print("kaydolabilir")
            cur.execute("INSERT into tohumschema.farmer ( mail, name, lastname, password, cityid) values(%s, %s, %s, %s, %s)", (email,first_name,last_name, first_password, city))
            cur.execute("SELECT farmerid from tohumschema.farmer where mail='{}'".format(email))
            farmerID = cur.fetchone()[0]
            con.commit()
        cur.close()

        return redirect(url_for("register"))

    else:
        return render_template('register.html',cities=cities)


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

            if name == "" and region == "" and opposite == "" and year == "" and area == "" and coefficient == "" and ton == "":
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1")
            elif name:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and name='{}'".format(name))
            elif region:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and r.regionid=(select regionid from tohumschema.region where regionname='{}')".format(region))
            elif opposite:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(opposite))
            elif year:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select productid from tohumschema.productdata where year={})".format(year))
            elif area:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select productid from tohumschema.productdata where area>{})".format(int(area)))
            elif coefficient:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.coefficient={}".format(int(coefficient)))
            elif  ton:
                cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select productid from tohumschema.productdata where ton>{})".format(int(ton)))

            data = None
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()

            return render_template('fruits.html',data=data)

        else:
            cur = con.cursor()
            #cur.execute("select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1")
            cur.execute("select * from tohumschema.product where type=1")
            x = cur.fetchall()
            cur.close()
            if x:
                return render_template('fruits.html', data=x)
            else:
                #hicbir data yoksa en basta
                return render_template('fruits.html', data=[-1,-1,-1,-1,-1])
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

@app.route('/medicines', methods=["POST","GET"])
def medicines():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        cur = con.cursor()
        cur.execute("SELECT  year, SUM(medicineamount) FROM tohumschema.data GROUP BY year")
        data = cur.fetchall()
        con.commit()
        cur.close()

        print("data",data)

        return render_template('medicines.html',data=data)

@app.route('/profile/overview', methods=["POST", "GET"])
def overview():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        return render_template('overview.html')

@app.route('/profile/settings', methods=["POST", "GET"])
def settings():

    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        return render_template('settings.html')

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










































