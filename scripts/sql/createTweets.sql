set input_format_import_nested_json=1;
CREATE TABLE IF NOT EXISTS TWITTER.tweets
(
    id UInt64,
    created_at DateTime,
    text String,
    full_text String, 
    is_retweet Boolean,
    lang String,
    USERID UInt64,
    USERNAME String,
    tweet_url String,
    retweet_id UInt64,
    retweet_created_at DateTime,
    retweet_user_id UInt64
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(created_at)
ORDER BY (USERID, created_at);