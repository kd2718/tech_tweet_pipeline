CREATE MATERIALIZED VIEW if not exists TWITTER.tweets_queue TO TWITTER.tweets AS 
SELECT *
FROM TWITTER.kafka_tweets_stream;