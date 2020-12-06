import csv
import psycopg2
from csv import reader


con = psycopg2.connect(host="localhost", port="5432", database="anket", user="postgres", password="facethest0rm")
#con = psycopg2.connect(host="localhost", port="9999", database="tohum", user="super", password="whqrnr&6mxAj7")

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
        print("INSERT INTO bolge VALUES ( " + row[0] + "," + row[1] + ")")
        sql_insert = "INSERT INTO bolge  VALUES ( " + row[0] + "," +"'"+row[1]+"'" + ");"

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
        print("INSERT INTO il VALUES ( " + row[1] + "," + row[2] + "," + row[0] + ")")
        sql_insert = "INSERT INTO il  VALUES ( " + row[1] + "," +"'"+row[2]+"' ," + row[0] + ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('district.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO ilce VALUES ( " + row[2] + "," +"'"+ row[3].strip() +"'"+ "," + row[0] + "," + row[1] + ");")
        print()
        sql_insert = "INSERT INTO ilce VALUES ( " + row[2] + "," +"'"+row[3].strip() +"'"+ "," + row[0] + "," + row[1] + ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('total_veri.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO veri VALUES ( " + row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + ");")
        print()
        sql_insert = "INSERT INTO veri VALUES ( " + row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('urun.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO urun VALUES ( " + row[0] + "," +"'"+ row[1] +"'"+ "," + row[2] + ");")
        print()
        sql_insert = "INSERT INTO urun VALUES ( " + row[0] + "," +"'"+ row[1] +"'"+ "," + row[2] + ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('meyve.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO meyve VALUES ( " + row[0] +  ");")
        print()
        sql_insert = "INSERT INTO meyve VALUES ( " + row[0] +  ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('sebze.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO sebze VALUES ( " + row[0] +  ");")
        print()
        sql_insert = "INSERT INTO sebze VALUES ( " + row[0] +  ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('tahil.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO tahil VALUES ( " + row[0] +  ");")
        print()
        sql_insert = "INSERT INTO tahil VALUES ( " + row[0] +  ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""

"""
with open('bakliyat.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    next(csv_reader)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        print()
        print("INSERT INTO bakliyat VALUES ( " + row[0] +  ");")
        print()
        sql_insert = "INSERT INTO bakliyat VALUES ( " + row[0] +  ");"

        cur.execute(sql_insert)
cur.close()
con.commit()
con.close()
"""