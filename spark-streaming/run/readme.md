### Spark container (run)


docker run -dit -p 8555:8080 -v /home/ubuntu/project/nba-event-processing/pipeline/spark-streaming/run/jars:/jars -p 7077:7077 -e INIT_DAEMON_STEP=setup_spark --name spark-master bde2020/spark-master:3.1.1-hadoop3.2

docker run -dit -p 8555:8080 -v /home/ubuntu:/jars -p 7077:7077 -e INIT_DAEMON_STEP=setup_spark --link kafka:kafka --name spark-worker bde2020/spark-master:3.1.1-hadoop3.2