# In production you would almost certainly limit the replication user must be on the follower (slave) machine,
# to prevent other clients accessing the log from other machines. For example, 'replicator'@'follower.acme.com'.
#
# However, this grant is equivalent to specifying *any* hosts, which makes this easier since the docker host
# is not easily known to the Docker container. But don't do this in production.
#
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replicator' IDENTIFIED BY 'replpass';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT  ON *.* TO 'debezium' IDENTIFIED BY 'dbz';

# Create the database that we'll use to populate data and watch the effect in the binlog
CREATE DATABASE wcd;
GRANT ALL PRIVILEGES ON wcd.* TO 'mysqluser'@'%';

# Switch to this database
USE wcd;

# Create and populate our products using a single insert with many rows
CREATE TABLE frame_data (
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  file_name VARCHAR(255) NOT NULL,
  fps INT,
  frame_num INT,
  frame_array JSON
);
ALTER TABLE frame_data AUTO_INCREMENT = 1001;

-- INSERT INTO frame_data
-- VALUES (default,"testrow2",20,1,'{"key1": "value1"}');

