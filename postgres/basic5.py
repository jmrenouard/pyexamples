#:Version:1.0.0
import psycopg2
import sys
from pprint import pprint
from ConfigParser import ConfigParser

import logging
logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG)
from logging import info
from logging import error
from logging import debug
from logging import warning

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

conf=config(section='output')

db = psycopg2.connect(**config())
cursor = db.cursor()

info ("This is the name of the script: %s" % sys.argv[0])
info ("Number of arguments: %d" % len(sys.argv))
info ("The arguments are: %s" % str(sys.argv))

for req in sys.argv[1:]:
    info ("-----------------------------------------")
    info ("-- "+ str(req) )
    info ("-----------------------------------------")
    if conf['type'] == 'JSON':
        cursor.execute("select array_to_json(array_agg(row_to_json(t))) from ("+str(req)+") t")
    elif conf['type'] == 'JSON_ONE':
        cursor.execute("select row_to_json(t) from ("+str(req)+") t")
    elif conf['type'] == 'SIMPLE':
        cursor.execute(str(req))
    else:    
        cursor.execute(str(req))
        
    numrows = cursor.rowcount
    info ("Number of result : %d" % numrows)
    list = cursor.fetchall()
    idx=1
    for d in list:
        info ("%d> %s" % (idx, str(d)))
        idx += 1
    info ("-----------------------------------------")
    info ("-- END OF "+ str(req) )
    info ("-----------------------------------------")
        
cursor.close ()
db.close()
