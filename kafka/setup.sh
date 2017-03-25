#!/bin/bash

echo "remove kafka and zookeeper"
docker rm -f kafka
docker rm -f zookeeper

# - set up zookeeper
echo "start zookeeper"
docker run \
    -d \
    -p 2181:2181 \
    -p 2888:2888 \
    -p 3888:3888 \
    --name zookeeper \
    confluent/zookeeper

# - wait for zookeeper to become stable
"wait zookeeper to become stable"
sleep 2

echo -n "Please enter your host for kafka(localhost/ip): "
read answer
export IP="$answer"

# - set up kafka
echo "start kafka"
docker run \
    -d \
    -p 9092:9092 \
    -e KAFKA_ADVERTISED_HOST_NAME="${IP}" \
    -e KAFKA_ADVERTISED_PORT=9092 \
    --name kafka \
    --link zookeeper:zookeeper \
    confluent/kafka

