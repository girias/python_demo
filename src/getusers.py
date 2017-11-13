"""#!/usr/bin/python"""
# import ConfigParser
import getpass
from config import configuration as config
import psycopg2

# __config__ = ConfigParser.ConfigParser()
# __config__.read("./config.txt")
# __database__ = __config__.get("configuration", "__database__")
__hostname__ = config.__db__['hostname']
__username__ = raw_input('Enter DB username:')
__password__ = getpass.getpass(prompt='Enter DB password ')
__database__ = config.__db__['database']

def get_all_users():
    """ select users from users table  """
    __select_users_sql__ = "SELECT first_name, last_name FROM public.users"
    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=__hostname__, user=__username__, \
                                password=__password__, dbname=__database__)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(__select_users_sql__)
        # print the users name
        for firstname, lastname in cur.fetchall():
            print firstname, lastname
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print error
    finally:
        if conn is not None:
            conn.close()
            