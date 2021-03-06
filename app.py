from flask import Flask, render_template, url_for, redirect, request, session, flash
import psycopg2
import datetime
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "hello"
con = psycopg2.connect(host="localhost", port="9999", database="tohumdb", user="super", password="whqrnr&6mxAj7")


@app.route('/', methods=["GET", "POST"])
def index():
    if "admin" in session or "user" in session:

        # Donat chart meta data about workers
        today = datetime.today()
        cur = con.cursor()
        cur.execute(
            "SELECT  year, SUM(workeramount) FROM tohumschema.data WHERE (year = {} ) GROUP BY year".format(today.year))
        data = cur.fetchone()

        cur = con.cursor()
        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year ORDER BY year")
        maxData = cur.fetchall()

        maxYear = today.year
        maxVal = 0
        lastYear = today.year - 1
        for i in maxData:
            if i[1] > maxVal:
                maxYear = i[0]
                maxVal = i[1]
            if i[0] == lastYear:
                lastYear = i

        percentDiff = format((maxVal - data[0]) / data[0] * 100, '.2f')

        lastPercentDiff = format((lastYear[1] - data[0]) / data[0] * 100, '.2f')

        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year")
        dataAll = cur.fetchall()
        con.commit()
        cur.close()

        # Line chart data about hectare distiribution

        cur = con.cursor()
        cur.execute("SELECT year, SUM(area) FROM tohumschema.productdata GROUP BY year;")
        dataArea = cur.fetchall()
        con.commit()
        cur.close()

        maxArea = 0
        minArea = 99999
        averageArea = 0
        for i in dataArea:
            averageArea += i[1]
            if i[1] > maxArea:
                maxArea = i[1]
            if i[1] < minArea:
                minArea = i[1]

        averageArea = float(format(averageArea / len(dataArea), '.2f'))

        maxAreaPercent = format((maxArea - averageArea) / averageArea * 100, '.2f')
        minAreaPercent = format((minArea - averageArea) / averageArea * 100, '.2f')

        # Bar chart about

        cur = con.cursor()
        cur.execute(
            "SELECT d.name, COUNT(dt.productid) FROM tohumschema.productdata dt, tohumschema.product d WHERE d.productid = dt.productid GROUP BY d.name;")
        dataProductString = cur.fetchall()
        con.commit()
        cur.close()

        maxProduct = 0
        maxProductLabel = ""

        minProduct = 999999
        minProductLabel = ""

        for i in dataProductString:
            if i[1] > maxProduct:
                maxProduct = i[1]
                maxProductLabel = i[0]
            if i[1] < minProduct:
                minProduct = i[1]
                minProductLabel = i[0]

        # account log output goes here

        cur = con.cursor()
        cur.execute(
            "SELECT f.name, s.opertype, s.logdatetime FROM tohumschema.systemlog s, tohumschema.farmer f  WHERE ((s.opertype = '1' or s.opertype = '2' or s.opertype = '3' or s.opertype = '4' or s.opertype = '5') and f.farmerid = s.farmerid)  ORDER BY s.logdatetime DESC;")
        dataAccountNamedLogs = cur.fetchall()
        con.commit()
        cur.close()

        # product log output goes here

        cur = con.cursor()
        cur.execute(
            "SELECT f.name, f.mail,s.opertype, s.logdatetime FROM tohumschema.systemlog s, tohumschema.farmer f  WHERE ((opertype = '4' or opertype = '5') and f.farmerid = s.farmerid) ORDER BY logdatetime DESC;")
        dataProductNamedLogs = cur.fetchall()
        con.commit()
        cur.close()

        return render_template('index.html', data="T", chartData=data, dataAll=dataAll, maxYear=maxYear, maxVal=maxVal,
                               percentDiff=percentDiff, lastPercentDiff=lastPercentDiff, lastYearData=lastYear,
                               dataArea=dataArea, minArea=minArea, maxArea=maxArea, averageArea=averageArea,
                               maxAreaPercent=maxAreaPercent, minAreaPercent=minAreaPercent,
                               dataProductString=dataProductString, maxProduct=maxProduct,
                               maxProductLabel=maxProductLabel
                               , minProductLabel=minProductLabel, minProduct=minProduct,
                               dataAccountNamedLogs=dataAccountNamedLogs, dataProductNamedLogs=dataProductNamedLogs)
    else:

        # Donat chart meta data about workers
        today = datetime.today()
        cur = con.cursor()
        cur.execute(
            "SELECT  year, SUM(workeramount) FROM tohumschema.data WHERE (year = {} ) GROUP BY year".format(today.year))
        data = cur.fetchone()

        cur = con.cursor()
        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year ORDER BY year")
        maxData = cur.fetchall()

        maxYear = today.year
        maxVal = 0
        lastYear = today.year - 1
        for i in maxData:
            if i[1] > maxVal:
                maxYear = i[0]
                maxVal = i[1]
            if i[0] == lastYear:
                lastYear = i

        percentDiff = format((maxVal - data[0]) / data[0] * 100, '.2f')

        lastPercentDiff = format((lastYear[1] - data[0]) / data[0] * 100, '.2f')

        cur.execute("SELECT  year, SUM(workeramount) FROM tohumschema.data GROUP BY year")
        dataAll = cur.fetchall()
        con.commit()
        cur.close()

        # Line chart data about hectare distiribution

        cur = con.cursor()
        cur.execute("SELECT year, SUM(area) FROM tohumschema.productdata GROUP BY year;")
        dataArea = cur.fetchall()
        con.commit()
        cur.close()

        maxArea = 0
        minArea = 99999
        averageArea = 0
        for i in dataArea:
            averageArea += i[1]
            if i[1] > maxArea:
                maxArea = i[1]
            if i[1] < minArea:
                minArea = i[1]

        averageArea = float(format(averageArea / len(dataArea), '.2f'))

        maxAreaPercent = format((maxArea - averageArea) / averageArea * 100, '.2f')
        minAreaPercent = format((minArea - averageArea) / averageArea * 100, '.2f')

        # Bar chart about

        cur = con.cursor()
        cur.execute(
            "SELECT d.name, COUNT(dt.productid) FROM tohumschema.productdata dt, tohumschema.product d WHERE d.productid = dt.productid GROUP BY d.name;")
        dataProductString = cur.fetchall()
        con.commit()
        cur.close()

        maxProduct = 0
        maxProductLabel = ""

        minProduct = 999999
        minProductLabel = ""

        for i in dataProductString:
            if i[1] > maxProduct:
                maxProduct = i[1]
                maxProductLabel = i[0]
            if i[1] < minProduct:
                minProduct = i[1]
                minProductLabel = i[0]

        # account log output goes here

        cur = con.cursor()
        cur.execute(
            "SELECT f.name, s.opertype, s.logdatetime FROM tohumschema.systemlog s, tohumschema.farmer f  WHERE ((s.opertype = '1' or s.opertype = '2' or s.opertype = '3' or s.opertype = '4' or s.opertype = '5') and f.farmerid = s.farmerid)  ORDER BY s.logdatetime DESC;")
        dataAccountNamedLogs = cur.fetchall()
        con.commit()
        cur.close()

        # product log output goes here

        cur = con.cursor()
        cur.execute(
            "SELECT f.name, f.mail,s.opertype, s.logdatetime FROM tohumschema.systemlog s, tohumschema.farmer f  WHERE ((opertype = '4' or opertype = '5') and f.farmerid = s.farmerid) ORDER BY logdatetime DESC;")
        dataProductNamedLogs = cur.fetchall()
        con.commit()
        cur.close()

        return render_template('index.html', data="T", chartData=data, dataAll=dataAll, maxYear=maxYear, maxVal=maxVal,
                               percentDiff=percentDiff, lastPercentDiff=lastPercentDiff, lastYearData=lastYear,
                               dataArea=dataArea, minArea=minArea, maxArea=maxArea, averageArea=averageArea,
                               maxAreaPercent=maxAreaPercent, minAreaPercent=minAreaPercent,
                               dataProductString=dataProductString, maxProduct=maxProduct,
                               maxProductLabel=maxProductLabel
                               , minProductLabel=minProductLabel, minProduct=minProduct,
                               dataAccountNamedLogs=dataAccountNamedLogs, dataProductNamedLogs=dataProductNamedLogs)


@app.route('/admin', methods=["POST", "GET"])
def admin():
    if "admin" not in session:
        return redirect(url_for("login"))
    else:
        return render_template("welcome.html", data="Admin")


@app.route('/user', methods=["POST", "GET"])
def user():
    if "user" in session:
        id = session.get("id", None)
        cur = con.cursor()
        cur.execute("select name from tohumschema.farmer where farmerid={}".format(id))
        x = cur.fetchone()[0]
        return render_template("welcome.html", data=x)
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

                cur = con.cursor()
                cur.execute(
                    "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 1, TIMESTAMP '{}' ) ".format(
                        session["id"], datetime.today()))
                con.commit()
                cur.close()

                return redirect(url_for("admin"))

            if truePassword == None:
                return redirect(url_for("login"))

            else:
                if password == truePassword.__str__():
                    session["user"] = "user"
                    session["id"] = id

                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 1, TIMESTAMP '{}' ) ".format(
                            session["id"], datetime.today()))
                    con.commit()
                    cur.close()

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
            cur.execute(
                "INSERT into tohumschema.farmer ( mail, name, lastname, password, cityid) values(%s, %s, %s, %s, %s)",
                (email, first_name, last_name, first_password, city))
            cur.execute("SELECT farmerid from tohumschema.farmer where mail='{}'".format(email))
            farmerID = cur.fetchone()[0]
            con.commit()

            cur2 = con.cursor()
            cur2.execute(
                "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 2, TIMESTAMP '{}' ) ".format(
                    farmerID, datetime.today()))
            con.commit()
            cur2.close()

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
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 group by p.name, p.coefficient, r.regionname, p.productid")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and name='{}' group by p.name, p.coefficient, r.regionname, p.productid".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and r.regionid={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and pd.year={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.area)>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 and p.coefficient={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.ton)>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
            except:
                pass
            cur.close()

            return render_template('fruits.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=1 group by p.name, p.coefficient, r.regionname, p.productid")
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
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 group by p.name, p.coefficient, r.regionname, p.productid")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and name='{}' group by p.name, p.coefficient, r.regionname, p.productid".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and r.regionid={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and pd.year={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.area)>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 and p.coefficient={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.ton)>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
            except:
                pass
            cur.close()

            return render_template('vegetables.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=2 group by p.name, p.coefficient, r.regionname, p.productid")
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
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 group by p.name, p.coefficient, r.regionname, p.productid")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and name='{}' group by p.name, p.coefficient, r.regionname, p.productid".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and r.regionid={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and pd.year={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.area)>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 and p.coefficient={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.ton)>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
            except:
                pass
            cur.close()

            return render_template('grains.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=3 group by p.name, p.coefficient, r.regionname, p.productid")
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
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 group by p.name, p.coefficient, r.regionname, p.productid")
            elif name:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and name='{}' group by p.name, p.coefficient, r.regionname, p.productid".format(
                        name))
            elif region:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and r.regionid={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        region))
            elif opposite:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, pd.area, pd.ton from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and p.productid=(select oppositeproductid from tohumschema.opposite where productid=(select productid from tohumschema.product where name='{}'))".format(
                        opposite))
            elif year:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and pd.year={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        year))
            elif area:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.area)>{}".format(
                        int(area)))
            elif coefficient:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 and p.coefficient={} group by p.name, p.coefficient, r.regionname, p.productid".format(
                        int(coefficient)))
            elif ton:
                cur.execute(
                    "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 group by p.name, p.coefficient, r.regionname, p.productid having sum(pd.ton)>{}".format(
                        int(ton)))

            data = None
            try:
                data = cur.fetchall()
            except:
                pass
            cur.close()

            return render_template('legumes.html', data=data)

        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, p.coefficient, r.regionname, sum(pd.area), sum(pd.ton) from tohumschema.product as p, tohumschema.region as r, tohumschema.productdata as pd where p.productid=pd.productid and p.regionid=r.regionid and p.type=4 group by p.name, p.coefficient, r.regionname, p.productid")
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

            cur2 = con.cursor()
            cur2.execute(
                "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 4, TIMESTAMP '{}' ) ".format(
                    session["id"], datetime.today()))
            con.commit()
            cur2.close()

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

                    cur2 = con.cursor()
                    cur2.execute(
                        "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 3, TIMESTAMP '{}' ) ".format(
                            session["id"], datetime.today()))
                    con.commit()
                    cur2.close()

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
        return render_template("tips.html", data=data)


@app.route('/profile/growings', methods=["POST", "GET"])
def growings():
    if "user" not in session and "admin" not in session:
        return redirect(url_for("login"))
    else:
        if request.method == "POST":

            if request.form["action"] == "Add":
                name = request.form["name"]
                area = request.form["area"]
                start_date = request.form["seedDate"]
                end_date = request.form["harvestDate"]
                cur = con.cursor()
                cur.execute("select productid from tohumschema.product where name='{}'".format(name))
                productid = cur.fetchone()[0]
                cur.execute(
                    "INSERT INTO tohumschema.growing (farmerid, productid, area, seeddate, harvestdate, status) VALUES ({}, {}, {}, TIMESTAMP '{}',TIMESTAMP '{}', 'waiting')".format(
                        session.get("id", None), productid, area, start_date, end_date))
                con.commit()
                cur.execute(
                    "select p.name, g.area, g.seeddate, g.harvestdate from tohumschema.product as p, tohumschema.growing as g where p.productid=g.productid and g.farmerid={} group by p.name, g.area, g.seeddate, g.harvestdate, p.productid".format(
                        session.get("id", None)))
                x = cur.fetchall()
                percents = percent_calculator(x)
                cur.close()
                return render_template("growing.html", data=zip(x, percents))
            elif request.form["action"] == "harvest":

                name = request.form["harvestName"]
                area = request.form["harvestArea"]
                ton  = request.form["harvestTon"]
                worker   = request.form["harvestWorker"]
                machine  = request.form["harvestMachine"]
                medicine = request.form["harvestMedicine"]
                start_date = request.form["harvestSeedDate"]
                end_date = request.form["harvestHarvestDate"]
                year = end_date.split("-")[0]


                cur2 = con.cursor()
                cur2.execute(
                    "INSERT INTO tohumschema.data  (farmerid, medicineamount,machineamount,workeramount,year) VALUES ( {} ,{}, {}, {},{});".format(
                        session["id"], medicine, machine, worker, year))
                con.commit()
                cur2.close()
                cur3 = con.cursor()
                cur3.execute("SELECT d.dataid FROM tohumschema.data d ORDER BY d.dataid DESC LIMIT 1")
                did = cur3.fetchone()[0]

                print(did)

                cur3.execute(
                    "INSERT INTO tohumschema.productdata ( dataid, productid, farmerid, area, ton, year ) VALUES({},(SELECT productid FROM tohumschema.product WHERE name = '{}'),{},{},{},{})".format(
                        did, name, session["id"], area, ton, year))
                con.commit()
                
                cur3.execute(
                    "DELETE FROM tohumschema.growing WHERE farmerid = {} AND productid = (SELECT productid FROM tohumschema.product WHERE name = '{}') AND area = {} AND seeddate =  TIMESTAMP '{}'".format(
                        session["id"], name, area, start_date))
                con.commit()

                cur = con.cursor()
                cur.execute("SELECT productid FROM tohumschema.product WHERE name = '{}'".format(name))
                productId = cur.fetchone()[0]
                cur.close()

                cur2 = con.cursor()
                cur2.execute(
                    "INSERT INTO tohumschema.systemlog ( farmerid, opertype, logdatetime )  VALUES ( {}, 5, TIMESTAMP '{}' ) ".format(
                        session["id"], datetime.today()))
                con.commit()
                cur2.close()


                cur = con.cursor()
                cur.execute(
                    "select p.name, g.area, g.seeddate, g.harvestdate, g.status from tohumschema.product as p, tohumschema.growing as g where p.productid=g.productid and g.farmerid={} group by p.name, g.area, g.seeddate, g.harvestdate, g.status, p.productid".format(
                        session.get("id", None)))
                x = cur.fetchall()
                percents = percent_calculator(x)
                cur.close()
                return render_template("growing.html", data=zip(x, percents))




        else:
            cur = con.cursor()
            cur.execute(
                "select p.name, g.area, g.seeddate, g.harvestdate, g.status from tohumschema.product as p, tohumschema.growing as g where p.productid=g.productid and g.farmerid={} group by p.name, g.area, g.seeddate, g.harvestdate, g.status, p.productid".format(
                    session.get("id", None)))
            x = cur.fetchall()
            percents = percent_calculator(x)
            cur.close()
            return render_template("growing.html", data=zip(x, percents))


def percent_calculator(x):
    data = [(row[2], row[3]) for row in x]
    percents = list()
    for row in data:
        start = row[0]
        end = row[1]
        start = start.strftime("%Y-%m-%d").split(sep="-")
        end = end.strftime("%Y-%m-%d").split(sep="-")
        end_date = date(int(end[0]), int(end[1]), int(end[2]))
        start_date = date(int(start[0]), int(start[1]), int(start[2]))
        today = date.today()
        total_diff = end_date - start_date
        today_diff = end_date - today
        percent = 100 - ((100 * today_diff.days) / total_diff.days)
        percents.append(percent)
    return percents


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
