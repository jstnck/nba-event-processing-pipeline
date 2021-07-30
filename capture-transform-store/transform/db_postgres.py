"""
Description: db.py can be imported to other scripts to make calls to postgres via psycopg2
"""


import psycopg2
from psycopg2 import OperationalError
import mysql.connector as mysql




# connects to postgres database, default port is 5432
def create_connection(db_name, db_host, db_user='postgres', db_password='postgres', db_port='5432'):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Connection to PostgreSQL DB successful")

    except OperationalError as e:
        print(f"the error '{e}' has occurred.")
    
    return connection

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        print("Query executed successfully.")
    
    except OperationalError as e:
        print(f"The error '{e}' has occurred.")

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        print("Query executed successfully.")

    except OperationalError as e:
        print(f"The error '{e}' has occurred.")

def insert_query(connection, query, records):
    # connection.autocommit = True
    cursor = connection.cursor()
    
    try:
        cursor.execute(query, records)
        connection.commit()

    except OperationalError as e:
        print(f"The error '{e}' has occurred.")

# def insert_query_v(connection, query, records):
#     connection.autocommit = True
#     cursor = connection.cursor()
    
#     try:
#         cursor.execute(query, records)
#         return("insert executed successfully")
#     except OperationalError as e:
#         return(f"The error '{e}' has occurred.")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# running the postgres docker-compose file locally - get ip address from docker
# db host is likely the ip address of a local container or a cloud server
def create_new_database(connection, db_name: str):
    ''' a wrapper around the 'create_database' function - don't need to pass in sql code
    by default uses existing 'connection' object'''
    
    try:
        # create the survey_tools database
        create_database_query = f"CREATE DATABASE {db_name}"
        create_database(connection, create_database_query)
    except OperationalError as e:
        print(f"The error '{e}' has occurred.")

# Define function using cursor.executemany() to insert the dataframe
def execute_many(conn, datafrm, table):
    
    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]
    
    # dataframe columns with Comma-separated
    cols = ','.join(list(datafrm.columns))
    

    pg_records = ", ".join(["%%s"] * len(datafrm.columns))
    # SQL query to execute
    sql = f"INSERT INTO %s(%s) VALUES({pg_records})" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(sql, tpls)
        conn.commit()
        print("Data inserted using execute_many() successfully...")
    except OperationalError as e:
        print(f"The error '{e}' has occurred.")