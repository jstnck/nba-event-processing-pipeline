### spark-streaming-with-debezium - guide
https://medium.com/@suchit.g/spark-streaming-with-kafka-connect-debezium-connector-ab9163808667


### sbt container (build)

docker run -it -v /home/ubuntu/project/nba-event-processing-pipeline/spark-streaming:/project hseeberger/scala-sbt:8u222_1.3.5_2.13.1

cd /project

$ sbt clean package   - sbt validates build

$ sbt clean assembly  - to generate a jar file


