#:Version:1.0.0
import psycopg2
import sys
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

print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: ", str(sys.argv)

for req in sys.argv[1:]:
    print "-----------------------------------------"
    print "-- " + str(req)
    print "-----------------------------------------"
    cursor.execute(str(req))
    numrows = cursor.rowcount
    print "Number of result :", numrows
    list = cursor.fetchall()
    for d in list:
        print "line :", str(d)
    print "-----------------------------------------"
    print "-- END OF " + str(req)
    print "-----------------------------------------"
        
cursor.close()
db.close()
