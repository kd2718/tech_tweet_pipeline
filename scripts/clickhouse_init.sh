#! /bin/bash

# help from this article
# https://medium.com/streamthoughts/how-to-build-a-real-time-analytical-platform-using-kafka-ksqldb-and-clickhouse-bfabd65d05e4


# create KAFKA table
echo $KAFKA_SERVER
clickhouse-client --query "drop database if exists TWITTER;"
clickhouse-client --query "CREATE DATABASE IF NOT EXISTS TWITTER"


clickhouse-client --query "drop table if exists TWITTER.kafka_tweets_stream;"
clickhouse-client --query "CREATE TABLE if not exists TWITTER.kafka_tweets_stream (\
    ID UInt64,\
    CREATEDAT DateTime,\
    TEXT String,\
    LANG String,\
    RETWEETED UInt8,\
    USERID UInt64,\
    USERNAME String,\
    USERLOCATION String,\
    HASHTAGS String,\
    MENTIONS String\
  ) ENGINE = Kafka SETTINGS \
    kafka_broker_list = 'kafka-main:29092', \
    kafka_topic_list = 'tech_twitter_stream', \
    kafka_group_name = 'tweet_group1',\
    kafka_format = 'JSONEachRow',\
    kafka_commit_every_batch = 1,\
    kafka_row_delimiter = '\n', \
    kafka_num_consumers = 1;"
    #kafka_group_name = 'ch-tweet-group',\
    #kafka_skip_broken_messages = 1,\
    #kafka_broker_list = '$KAFKA_SERVER',\
    #kafka_topic_list = '$KAFKA_TOPIC',\

# create clickhouse table
clickhouse-client --query "CREATE TABLE IF NOT EXISTS TWITTER.tweets\
(\
    ID UInt64,\
    CREATEDAT DateTime,\
    TEXT String,\
    LANG String,\
    RETWEETED UInt8,\
    USERID UInt64,\
    USERNAME String,\
    USERDESCRIPTION String,\
    USERLOCATION String,\
    HASHTAGS String,\
    MENTIONS String\
) ENGINE = MergeTree()\
PARTITION BY toYYYYMM(CREATEDAT)\
ORDER BY (USERID, CREATEDAT);"


# more help
# https://altinity.com/blog/2020/5/21/clickhouse-kafka-engine-tutorial

# create materialized view
clickhouse-client --query "CREATE MATERIALIZED VIEW if not exists TWITTER.tweets_queue TO TWITTER.tweets AS \
SELECT *
FROM TWITTER.kafka_tweets_stream;"