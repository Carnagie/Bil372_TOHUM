import csv
import psycopg2
from csv import reader


con = psycopg2.connect(host="localhost", port="5432", database="tohumdb", user="postgres", password="facethest0rm")
#con = psycopg2.connect(host="localhost", port="9999", database="tohumdb", user="super", password="whqrnr&6mxAj7")

cur = con.cursor()

"""
with open('state.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print("INSERT INTO tohumschema.region VALUES ( " + row[0] + "," + row[1] + ")")
        sql_insert = "INSERT INTO tohumschema.region  VALUES ( " + row[0] + "," +"'"+row[1]+"'" + ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""


"""
with open('city.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print("INSERT INTO tohumschema.city VALUES ( " + row[0] + "," + row[1] + "," + row[2] + ")")
        sql_insert = "INSERT INTO tohumschema.city  VALUES ( " + row[0] + "," + row[1] +",'"+ row[2] + "'"+");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""
