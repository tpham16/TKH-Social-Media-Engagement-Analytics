DROP SCHEMA IF EXISTS market cascade;
CREATE SCHEMA market;

CREATE TABLE market.youtube(
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255),
    url VARCHAR(255),
    viewCount INT,
    date VARCHAR(255),
    likes INT,
    duration VARCHAR(255),
    commentsCount FLOAT
);

CREATE TABLE market.twitter(
    id VARCHAR(255) PRIMARY KEY,
    twitter_date DATE,
    Tweet VARCHAR(1000),
    Likes INT,
    Comments INT,
    Retweets INT
    
);

DROP TABLE IF EXISTS market.instagram CASCADE ;
DROP TABLE IF EXISTS market.instagram_hashtag CASCADE;
DROP TABLE IF EXISTS market.instagram_hash_post CASCADE;

CREATE TABLE market.instagram(
    id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255), 
    commentsCount FLOAT,
    likesCount FLOAT,
    ig_timestamp timestamp,
    videoViewCount FLOAT,
    videoPlayCount FLOAT,
    videoDuration FLOAT    
);
CREATE TABLE market.instagram_hashtag(
    index_num int PRIMARY KEY,
    hashtag VARCHAR(255)
);
CREATE TABLE market.instagram_hash_post(
    index INT PRIMARY KEY,
    id VARCHAR(255) REFERENCES market.instagram(id),
    hashtag_index float REFERENCES market.instagram_hashtag(index_num)
);
-- Create TABLE market.facebook
-- CREATE TABLE market.linkedin
