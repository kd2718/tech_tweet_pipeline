set input_format_import_nested_json=1;
CREATE TABLE if not exists TWITTER.kafka_tweets_stream 
(
    id UInt64,
    created_at DateTime,
    text String,
    full_text String,
    is_retweet Boolean,
    lang String null,
    USERID UInt64,
    USERNAME String,
    tweet_url String,
    retweet_id UInt64,
    retweet_created_at DateTime,
    retweet_user_id UInt64
  ) ENGINE = Kafka SETTINGS 
    kafka_broker_list = 'kafka:9092', 
    kafka_topic_list = 'tech_twitter_stream', 
    kafka_group_name = 'tweet_group1',
    kafka_format = 'JSONEachRow',
    kafka_commit_every_batch = 1,
    kafka_num_consumers = 1;