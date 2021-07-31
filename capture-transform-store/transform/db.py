"""
Description: db.py can be imported to other scripts to make calls to mysql db
"""


import mysql.connector as mysql
import logging

def create_connection(db_host: str, db_user: str, db_password: str, db_port: int=3306):
    """ creates a connection object with mysql """
    connection = None
    try:
        with mysql.connect(
            host=db_host,
            user=db_user,
            passwd=db_password,
        ) as connection:
            return connection
    except mysql.Error as e:
        return (e)


def insert_query(connection, query):
    """ inserts a single row into mysql """
    try:
        connection.reconnect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logging.info('row inserted successfully')
    except mysql.Error as e:
        logging.info(f'an error occurred at row insert: {e}')
        return (e)
