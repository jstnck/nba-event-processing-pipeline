import db


db_name = "postgres"
host_ip = "172.16.57.3"

# can use docker inspect to get postgres container ip address

# souce your DB_USER and DB_PASSWORD as environment variables
connection = db.create_connection(
    db_name=db_name, 
    db_host=host_ip
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

drop_table_string = """ 
DROP TABLE IF EXISTS frame_data
"""


db.execute_query(connection, drop_table_string)
db.execute_query(connection, create_table_string)
