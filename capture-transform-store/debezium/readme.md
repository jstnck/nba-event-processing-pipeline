## To run debezium containers individually:


#### zookeeper 
docker run -dit --name zookeeper -p 2181:2181 -p 2888:2888 -p 3888:3888 debezium/zookeeper:1.5


#### kafka
docker run -dit --name kafka -p 9092:9092 --link zookeeper:zookeeper debeziu/kafka:1.5

#### kafka connect
docker run -dit --name connect -p 8083:8083 -e GROUP_ID=1 -e CONFIG_STORAGE_TOPIC=my_connect_configs -e OFFSET_STORAGE_TOPIC=my_connect_offsets -e STATUS_STORAGE_TOPIC=my_connect_statuses --link zookeeper:zookeeper --link kafka:kafka --link mysql:mysql debezium/connect:1.5





#### list connectors
curl -H "Accept:application/json" localhost:8083/connectors/



#### postgres connector config

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


#### to create a postgres connector
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "pg-connector", "config": { "connector.class": "io.debezium.connector.postgresql.PostgresConnector", "tasks.max": "1", "database.hostname": "store", "database.port": "5432", "database.user": "postgres", "database.password": "postgres", "database.dbname": "postgres", "database.server.id": "184054", "database.server.name": "dbserver1", "database.include.list": "postgres", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.inventory" } }'



#### find the topic in kafka container
bin/kafka-topics.sh --list --zookeeper zookeeper

#### get a topic stream in the kafka console
bin/kafka-console-consumer.sh --topic dbserver1.postgres.frame_data --bootstrap-server [containerID]:9092

