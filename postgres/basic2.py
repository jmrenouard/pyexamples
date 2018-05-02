# Version:1.0.0
import psycopg2
import configparser


def get_config(filename='database.ini', section='postgresql'):
    # create a parser
    config = configparser.ConfigParser()
    # read config file
    config.read(filename)

    # get section, default to postgresql
    res = {}
    if config.has_section(section):
        params = config.items(section)
        for param in params:
            res[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return res


db = psycopg2.connect(**get_config())
cursor = db.cursor()
cursor.execute("Select datname from pg_database")
numrows = cursor.rowcount
print("Number of databases :", numrows)
liste = cursor.fetchall()
for d in liste:
    print("Database :", d)
cursor.close()
db.close()
