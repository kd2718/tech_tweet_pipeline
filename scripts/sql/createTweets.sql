CREATE TABLE IF NOT EXISTS TWITTER.tweets
(
    id UInt64,
    id_str String, 
    created_at DateTime,
    text String,
    lang String,
    user Nested ( 
      id UInt64, 
      name String 
    ), 
    USERID UInt64,
    USERNAME String,
    USERDESCRIPTION String,
    USERLOCATION String,
    HASHTAGS String,
    test_dat Int8, 
    MENTIONS String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(created_at)
ORDER BY (USERID, created_at);