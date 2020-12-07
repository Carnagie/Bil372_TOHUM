from flask import Flask, render_template, url_for, redirect, request, session, flash
import psycopg2
import datetime
from datetime import datetime

app = Flask(__name__)
app.secret_key = "hello"
con = psycopg2.connect(host="localhost", port="9999", database="tohumdb", user="super", password="whqrnr&6mxAj7")


@app.route('/', methods=["GET", "POST"])
def index():
    if "admin" in session or "user" in session:

        today = datetime.today()
        cur = con.cursor()
        cur.execute(
            "SELECT  year, SUM(workeramount) FROM tohumschema.data WHERE (year = {} ) GROUP BY year".format(today.year))
        data = cur.fetchone()

        cur = con.cursor()
        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year ORDER BY year")
        maxData = cur.fetchall()

        print(maxData)

        maxYear = today.year
        maxVal = 0
        lastYear = today.year - 1
        for i in maxData:
            if i[1] > maxVal:
                maxYear = i[0]
                maxVal = i[1]
            if i[0] == 2019:
                lastYear = i

        percentDiff = format((maxVal - data[0]) / data[0] * 100, '.2f')

        lastPercentDiff = format((lastYear[1] - data[0]) / data[0] * 100, '.2f')

        print(maxYear, maxVal, percentDiff)
        print(lastYear)

        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year")
        dataAll = cur.fetchall()
        con.commit()
        cur.close()

        return render_template('index.html', data="T", chartData=data, dataAll=dataAll, maxYear=maxYear, maxVal=maxVal,
                               percentDiff=percentDiff, lastPercentDiff=lastPercentDiff)
    else:

        today = datetime.today()
        cur = con.cursor()
        cur.execute(
            "SELECT  year, SUM(workeramount) FROM tohumschema.data WHERE (year = {} ) GROUP BY year".format(today.year))
        data = cur.fetchone()

        cur = con.cursor()
        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year ORDER BY year")
        maxData = cur.fetchall()

        print(maxData)

        maxYear = today.year
        maxVal = 0
        lastYear = today.year - 1
        for i in maxData:
            if i[1] > maxVal:
                maxYear = i[0]
                maxVal = i[1]
            if i[0] == 2019:
                lastYear = i

        percentDiff = format((maxVal - data[0]) / data[0] * 100, '.2f')

        lastPercentDiff = format((lastYear[1] - data[0]) / data[0] * 100, '.2f')

        print(maxYear, maxVal, percentDiff)
        print(lastYear)

        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year")
        dataAll = cur.fetchall()
        con.commit()
        cur.close()

        return render_template('index.html', data="F", chartData=data, dataAll=dataAll, maxYear=maxYear, maxVal=maxVal,
                               percentDiff=percentDiff, lastPercentDiff=lastPercentDiff)


@app.route('/admin', methods=["POST", "GET"])
def admin():
    if "admin" not in session:
        return redirect(url_for("login"))
    else:
        return "admin sayfasi"


@app.route('/user', methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        return "user sayfasi"
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=["POST", "GET"])
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
            cur.execute("select farmerid,password from tohumschema.farmer where mail='{}'".format(email))
            data = cur.fetchone()
            truePassword = data[1]
            id = data[0]
            con.commit()
            cur.close()

            if email == "admin@admin.com" and password == "admin":
                session["admin"] = "admin"
                session["id"] = 1
                return redirect(url_for("admin"))

            if truePassword == None:
                return redirect(url_for("login"))

            else:
                if password == truePassword.__str__():
                    session["user"] = "user"
                    session["id"] = id
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
    session.pop("id", None)
    return redirect(url_for("login"))


@app.route('/register', methods=["POST", "GET"])
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
            cur.execute(
                "INSERT into tohumschema.farmer ( mail, name, lastname, password, cityid) values(%s, %s, %s, %s, %s)",
                (email, first_name, last_name, first_password, city))
            cur.execute("SELECT farmerid from tohumschema.farmer where mail='{}'".format(email))
            farmerID = cur.fetchone()[0]
            con.commit()
        cur.close()

        return redirect(url_for("register"))

    else:
        return render_template('register.html', cities=cities)


@app.route('/fruits', methods=["POST", "GET"])
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
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and name='{}'".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and r.regionid={}".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and pd.year={}".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and pd.area>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.coefficient={}".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and pd.ton>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()

            return render_template('fruits.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1")
            x = cur.fetchall()
            cur.close()
            if x:
                return render_template('fruits.html', data=x)
            else:
                # hicbir data yoksa en basta
                return render_template('fruits.html', data=[-1, -1, -1, -1, -1])


@app.route('/vegetables', methods=["POST", "GET"])
def vegatables():
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
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and name='{}'".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and r.regionid={}".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and pd.year={}".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and pd.area>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and p.coefficient={}".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and pd.ton>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()

            return render_template('vegetables.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2")
            x = cur.fetchall()
            cur.close()
            if x:
                return render_template('vegetables.html', data=x)
            else:
                # hicbir data yoksa en basta
                return render_template('vegetables.html', data=[-1, -1, -1, -1, -1])


@app.route('/grains', methods=["POST", "GET"])
def grains():
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
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and name='{}'".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and r.regionid={}".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and pd.year={}".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and pd.area>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and p.coefficient={}".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and pd.ton>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()

            return render_template('grains.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3")
            x = cur.fetchall()
            cur.close()
            if x:
                return render_template('grains.html', data=x)
            else:
                # hicbir data yoksa en basta
                return render_template('grains.html', data=[-1, -1, -1, -1, -1])


@app.route('/legumes', methods=["POST", "GET"])
def legumes():
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
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and name='{}'".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and r.regionid={}".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and pd.year={}".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and pd.area>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and p.coefficient={}".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and pd.ton>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
                print(data)
            except:
                print("no fetch")
            cur.close()

            return render_template('legumes.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4")
            x = cur.fetchall()
            cur.close()
            if x:
                return render_template('legumes.html', data=x)
            else:
                # hicbir data yoksa en basta
                return render_template('legumes.html', data=[-1, -1, -1, -1, -1])


@app.route('/medicines', methods=["POST", "GET"])
def medicines():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        startdate = -1
        enddate = -1
        cur = con.cursor()
        cur.execute("SELECT  year, SUM(medicineamount) FROM tohumschema.data GROUP BY year")
        data = cur.fetchall()
        con.commit()
        cur.close()

        if request.method == "POST":
            startdate = request.form["start"]
            enddate = request.form["end"]

            cur = con.cursor()
            cur.execute("SELECT  year, SUM(medicineamount) FROM tohumschema.data WHERE ( year > " + str(
                startdate) + " AND " + str(enddate) + " > year ) GROUP BY year")
            data = cur.fetchall()
            con.commit()
            cur.close()

        print(data)

        return render_template('medicines.html', data=data, startdate=startdate, enddate=enddate)


@app.route('/machines', methods=["POST", "GET"])
def machines():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        startdate = -1
        enddate = -1
        cur = con.cursor()
        cur.execute("SELECT  year, SUM(machineamount) FROM tohumschema.data GROUP BY year")
        data = cur.fetchall()
        con.commit()
        cur.close()

        if request.method == "POST":
            startdate = request.form["start"]
            enddate = request.form["end"]

            cur = con.cursor()
            cur.execute("SELECT  year, SUM(machineamount) FROM tohumschema.data WHERE ( year > " + str(
                startdate) + " AND " + str(enddate) + " > year ) GROUP BY year")
            data = cur.fetchall()
            con.commit()
            cur.close()

        print(data)

        return render_template('machines.html', data=data, startdate=startdate, enddate=enddate)


@app.route('/workers', methods=["POST", "GET"])
def workers():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        startdate = -1
        enddate = -1
        cur = con.cursor()
        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year")
        data = cur.fetchall()
        con.commit()
        cur.close()

        if request.method == "POST":
            startdate = request.form["start"]
            enddate = request.form["end"]

            cur = con.cursor()
            cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data WHERE ( year > " + str(
                startdate) + " AND " + str(enddate) + " > year ) GROUP BY year")
            data = cur.fetchall()
            con.commit()
            cur.close()

        print(data)

        return render_template('workers.html', data=data, startdate=startdate, enddate=enddate)


@app.route('/profile/data', methods=["POST", "GET"])
def adddata():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        cur = con.cursor()
        cur.execute(
            "SELECT p.name, pd.area, pd.ton, d.medicineamount, d.workeramount, d.machineamount FROM tohumschema.data d JOIN tohumschema.productdata pd ON d.dataid=pd.dataid JOIN tohumschema.product p ON pd.productid=p.productid WHERE d.farmerid = {} ORDER BY d.dataid DESC LIMIT 10".format(
                session["id"]))
        latest1 = cur.fetchall()
        cur.close()

        print(session["id"])

        if request.method == "POST":
            name = request.form["name"]
            area = request.form["area"]
            weight = request.form["weight"]
            medicine = request.form["medicine"]
            worker = request.form["worker"]
            machine = request.form["machine"]
            year = request.form["year"]
            cur2 = con.cursor()

            cur2.execute(
                "INSERT INTO tohumschema.data  (farmerid, medicineamount,machineamount,workeramount,year) VALUES ( {} ,{}, {}, {},{});".format(
                    session["id"], medicine, machine, worker, year))
            con.commit()
            cur2.close()
            cur3 = con.cursor()
            cur3.execute("SELECT d.dataid FROM tohumschema.data d ORDER BY d.dataid DESC LIMIT 1")
            did = cur3.fetchone()[0]

            cur3.execute(
                "INSERT INTO tohumschema.productdata ( dataid, productid, farmerid, area, ton, year ) VALUES({},(SELECT productid FROM tohumschema.product WHERE name = '{}'),{},{},{},{})".format(
                    did, name, session["id"], area, weight, year))
            con.commit()
            cur3.execute(
                "SELECT p.name, pd.area, pd.ton, d.medicineamount, d.workeramount, d.machineamount FROM tohumschema.data d JOIN tohumschema.productdata pd ON d.dataid=pd.dataid JOIN tohumschema.product p ON pd.productid=p.productid WHERE d.farmerid = " +
                str(session["id"]) + " ORDER BY d.dataid DESC LIMIT 10")
            latest = cur3.fetchall()
            cur3.close()

            return render_template('adddata.html', data=latest)
        else:
            return render_template('adddata.html', data=latest1)


@app.route('/profile/overview', methods=["POST", "GET"])
def overview():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        cur = con.cursor()
        x = session.get("id", None)
        if x:
            cur.execute(
                "select f.name, f.lastname, c.cityname from tohumschema.farmer as f, tohumschema.city as c where f.cityid=c.cityid and f.farmerid={}".format(
                    x))
            data = cur.fetchone()
            return render_template('overview.html', data=data)


@app.route('/profile/settings', methods=["POST", "GET"])
def settings():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        cur = con.cursor()
        x = session.get("id", None)
        cur.execute(
            "select f.name, f.lastname, c.cityname, f.mail from tohumschema.farmer as f, tohumschema.city as c where f.cityid=c.cityid and f.farmerid={}".format(
                x))
        data = cur.fetchone()
        cur.execute(
            "select f.name, f.lastname, f.mail, c.cityname, f.password from tohumschema.farmer as f, tohumschema.city as c where f.cityid=c.cityid and f.farmerid={}".format(
                x))
        values = cur.fetchone()
        if request.method == "POST":
            name = request.form["name"]
            lastname = request.form["lastname"]
            email = request.form["email"]
            city = request.form["city"]
            old_password = request.form["password"]
            new_password = request.form["newpassword"]
            new_password2 = request.form["newpassword2"]

            if name != values[0]:
                cur.execute(
                    "update tohumschema.farmer set name = '{}' where farmerid = {}".format(name, x)
                )
            if lastname != values[1]:
                cur.execute(
                    "update tohumschema.farmer set lastname = '{}' where farmerid = {}".format(lastname, x)
                )
            if email != values[2]:
                cur.execute(
                    "update tohumschema.farmer set mail = '{}' where farmerid = {}".format(email, x)
                )
            if city != values[3]:
                cur.execute(
                    "select cityid from tohumschema.city where cityname='{}'".format(city)
                )
                data2 = cur.fetchone()
                print(data2[0])
                cur.execute(
                    "update tohumschema.farmer set cityid =  {} where farmerid = {}".format(data2[0], x)
                )
            if old_password != values[4]:
                print("eski sifre hatali")
                return redirect(url_for("settings"))
            else:
                if new_password != new_password2:
                    print("sifreler uyusmuyor")
                    return redirect(url_for("settings"))
                else:
                    cur.execute(
                        "update tohumschema.farmer set password = '{}' where farmerid = {}".format(new_password, x)
                    )
                    return redirect(url_for("settings"))

        else:
            return render_template('settings.html', data=data)


@app.route('/profile/tips', methods=["POST", "GET"])
def tips():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        cur = con.cursor()
        cur.execute(
            "select name, sum(area), sum(ton) from tohumschema.productdata join tohumschema.product on tohumschema.productdata.productid=tohumschema.product.productid where year=2020 group by productdata.productid, name order by sum(ton) desc limit 8")
        data = cur.fetchall()
        print(data)
        return render_template("tips.html", data=data)


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
