
pgadmin volume must be set so that the conainer can read/write in the directory
https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#mapped-files-and-directories

sudo chown -R 5050:5050 <host_directory>

sudo chown -R 5050:5050 pgadmin-vol