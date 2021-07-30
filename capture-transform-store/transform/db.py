"""
Description: db.py can be imported to other scripts to make calls to mysql db
"""


import mysql.connector as mysql


def create_connection(db_host: str, db_user: str, db_password: str, db_port: int=3306):
    connection = None
    try:
        with mysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
        ) as connection:
            return connection
    except mysql.Error as e:
        return (e)


def insert_query(connection, query, records):
    # connection.autocommit = True
    cursor = connection.cursor()
    
    try:
        cursor.execute(query, records)
        connection.commit()

    except mysql.Error as e:
        return (e)
