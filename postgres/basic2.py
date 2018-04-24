#:Version:1.0.0
import psycopg2
from ConfigParser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

db = psycopg2.connect(**config())
cursor = db.cursor()
cursor.execute("Select datname from pg_database")
numrows = cursor.rowcount
print "Number of databases :", numrows
list = cursor.fetchall()
for d in list:
    print "Database :", d
cursor.close ()
db.close()
