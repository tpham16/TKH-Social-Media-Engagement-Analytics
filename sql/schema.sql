DROP SCHEMA IF EXISTS market cascade;
CREATE SCHEMA market;

CREATE TABLE market.youtube(
    index VARCHAR(255),
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255),
    url VARCHAR(255),
    viewCount VARCHAR(255),
    date VARCHAR(255),
    likes VARCHAR(255),
    duration VARCHAR(255),
    commentsCount VARCHAR(255)
);

CREATE TABLE market.twitter(
    id VARCHAR(255) PRIMARY KEY,
    Likes INT,
    Comments INT,
    Reposts INT,
    twitter_date DATE
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
