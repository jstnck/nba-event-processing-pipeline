## To run debezium containers individually:


#### zookeeper 
docker run -it --rm --name zookeeper -p 2181:2181 -p 2888:2888 -p 3888:3888 debezium/zookeeper:1.5


#### kafka
docker run -it --rm --name kafka -p 9092:9092 --link zookeeper:zookeeper debezium/kafka:1.5

#### kafka connect
docker run -dit --name connect -p 8083:8083 -e GROUP_ID=1 -e CONFIG_STORAGE_TOPIC=my_connect_configs -e OFFSET_STORAGE_TOPIC=my_connect_offsets -e STATUS_STORAGE_TOPIC=my_connect_statuses --link zookeeper:zookeeper --link kafka:kafka --link store:store debezium/connect:1.5

#### database
docker run -it --rm --name store -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres debezium/example-postgres:1.5


#### list connectors
curl -H "Accept:application/json" localhost:8083/connectors/



#### postgres connector config example:

{
	"name": "pg-connector",
	"config": {
		"connector.class": "io.debezium.connector.postgresql.PostgresConnector",
		"database.hostname": "store",
		"database.port": "5432",
		"database.user": "postgres",
		"database.password": "postgres",
		"database.server.name": "postgres",
		"database.include.list": "postgres",
		"database.history.kafka.bootstrap.servers": "kafka:9092",
		"database.history.kafka.topic": "dbhistory.postgres"
	}
}


#### mysql connector config:
{
	"name": "wcd-connector",
	"config": {
		"connector.class": "io.debezium.connector.mysql.MySqlConnector",
		"tasks.max": "1",
		"database.hostname": "store",
		"database.port": "3306",
		"database.user": "root",
		"database.password": "debezium",
		"database.server.id": "184056",
		"database.server.name": "dbserver1",
		"database.include.list": "wcd",
		"database.history.kafka.bootstrap.servers": "kafka:9092",
		"database.history.kafka.topic": "dbhistory.wcd"
	}
}


#### to create a postgres connector
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "pg-connector", "config": { "connector.class": "io.debezium.connector.postgresql.PostgresConnector", "tasks.max": "1", "database.hostname": "store", "database.port": "5432", "database.user": "postgres", "database.password": "postgres", "database.dbname": "postgres", "database.server.id": "184054", "database.server.name": "dbserver1", "database.include.list": "postgres", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.postgres" } }'

(without database.server.id)
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "pg-connector", "config": { "connector.class": "io.debezium.connector.postgresql.PostgresConnector", "tasks.max": "1", "database.hostname": "store", "database.port": "5432", "database.user": "postgres", "database.password": "postgres", "database.dbname": "postgres", "database.server.name": "dbserver1", "database.include.list": "postgres", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.postgres" } }'

#### find the topic in kafka container 
bin/kafka-topics.sh --list --zookeeper zookeeper:2181

#### get a topic stream in the kafka console
bin/kafka-console-consumer.sh --topic dbserver1.wcd.frame_data --bootstrap-server [containerID]:9092

#### view history of topic 
bin/kafka-console-consumer.sh --topic dbserver1.wcd.frame_data --from-beginning --bootstrap-server [containerID]:9092






#### tutorial config commands

docker run -it --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw debezium/example-mysql:1.5

docker run -it --rm --name connect -p 8083:8083 -e GROUP_ID=1 -e CONFIG_STORAGE_TOPIC=my_connect_configs -e OFFSET_STORAGE_TOPIC=my_connect_offsets -e STATUS_STORAGE_TOPIC=my_connect_statuses --link zookeeper:zookeeper --link kafka:kafka --link mysql:mysql debezium/connect:1.5

docker run -it --rm --name store -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres debezium/example-postgres:1.5




postgres

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "pg-connector", "config": { "connector.class": "io.debezium.connector.postgresql.PostgresConnector", "tasks.max": "1", "database.hostname": "store", "database.port": "5432", "database.user": "postgres", "database.password": "postgres", "database.dbname": "postgres", "database.server.id": "184054", "database.server.name": "dbserver1", "database.include.list": "new", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.postgres" } }'




mysql / store

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "frame_data-connector", "config": { "connector.class": "io.debezium.connector.mysql.MySqlConnector", "tasks.max": "1", "database.hostname": "store", "database.port": "3306", "database.user": "debezium", "database.password": "dbz", "database.server.id": "184054", "database.server.name": "dbserver1", "database.include.list": "wcd", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.wcd" } }'

