import db


# souce your DB_USER and DB_PASSWORD as environment variables
connection = db.create_connection(
    db_name="postgres", 
    db_user="postgres", 
    db_password="postgres", 
    db_host="localhost"
    )

# create questions_structure table
create_table_string = """
CREATE TABLE IF NOT EXISTS frame_data (
    id SERIAL,
    file_name VARCHAR(255),
    fps INT,
    frame_num INT,
    frame_data JSON,
    PRIMARY KEY (file_name, frame_num)
)
"""

db.execute_query(connection, create_table_string)
