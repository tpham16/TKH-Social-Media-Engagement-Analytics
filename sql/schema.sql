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
    Tweet VARCHAR(255),
    Likes INT,
    Comments INT,
    Retweets INT
    
);

CREATE TABLE market.instagram(
    id VARCHAR(255) PRIMARY KEY,
    hashtags VARCHAR(255),
    commentsCount INT,
    likesCount INT,
    ig_timestamp timestamp,
    videoViewCount INT,
    videoPlayCount INT,
    videoDuration INT    
);

-- Create TABLE market.facebook
-- CREATE TABLE market.linkedin
