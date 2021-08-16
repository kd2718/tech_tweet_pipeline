CREATE TABLE if not exists TWITTER.kafka_tweets_stream (
    id UInt64,
    id_str String,
    created_at DateTime,
    text String,
    lang String null,
    user Nested ( 
      id UInt64, 
      name String 
    ), 
    USERID UInt64,
    USERNAME String,
    USERLOCATION String,
    HASHTAGS String,
    test_dat Int8, 
    MENTIONS String
  ) ENGINE = Kafka SETTINGS 
    kafka_broker_list = 'kafka:9092', 
    kafka_topic_list = 'tech_twitter_stream', 
    kafka_group_name = 'tweet_group1',
    kafka_format = 'JSONEachRow',
    kafka_commit_every_batch = 1,
    kafka_num_consumers = 1;