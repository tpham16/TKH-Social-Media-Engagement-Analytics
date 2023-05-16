DROP SCHEMA IF EXISTS market cascade;
CREATE SCHEMA market;

CREATE TABLE market.youtube(
    id VARCHAR(255) PRIMARY KEY,
    youtube_date DATE,
    Likes INT,
    CommentCount INT,
    ViewCount INT,
    Title VARCHAR(255),
    URL VARCHAR(255)
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