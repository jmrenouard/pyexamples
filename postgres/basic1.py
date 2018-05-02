# /usr/bin/python3
import psycopg2

db = psycopg2.connect("host=localhost dbname=template1 user=postgres")
cursor = db.cursor()
cursor.execute("Select datname from pg_database")
numrows = cursor.rowcount
print("Number of databases :", numrows)
liste = cursor.fetchall()
for d in liste:
    print("Database :", d)
cursor.close()
db.close()
