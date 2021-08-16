#! /bin/bash

# help from this article
# https://medium.com/streamthoughts/how-to-build-a-real-time-analytical-platform-using-kafka-ksqldb-and-clickhouse-bfabd65d05e4


# create KAFKA table
echo $KAFKA_SERVER
clickhouse-client --query "drop database if exists TWITTER;"
clickhouse-client --query "CREATE DATABASE IF NOT EXISTS TWITTER"


clickhouse-client --query "drop table if exists TWITTER.kafka_tweets_stream;"
clickhouse-client --query "drop table if exists TWITTER.tweets"
clickhouse-client --query "drop view if exists TWITTER.tweets_queue"

clickhouse-client --queries-file /opt/scripts/sql/createStream.sql /opt/scripts/sql/createTweets.sql /opt/scripts/sql/createView.sql

