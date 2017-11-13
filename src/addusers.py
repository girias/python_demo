"""#!/usr/bin/python"""
import getpass
import config.configuration as config
import psycopg2


__hostname__ = config.__db__['hostname']
__username__ = raw_input('Enter DB username:')
__password__ = getpass.getpass(prompt='Enter DB password: ')
__database__ = config.__db__['database']

def insert_users(__users__):
    """ insert multiple users into the users table  """
    __insert_users_sql__ = "INSERT INTO public.users\
            (first_name,last_name,lan_id, email_id, internal, company_name) \
            VALUES (%(first_name)s, %(last_name)s, %(lan_id)s,%(email_id)s, \
            %(internal)s, %(company_name)s)"
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
        cur.executemany(__insert_users_sql__, __users__)
        # commit the changes to the database
        conn.commit()
        print 'Users added successfully'
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print error
    finally:
        if conn is not None:
            conn.close()
