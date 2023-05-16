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
    row_index INT PRIMARY KEY,
    ID VARCHAR(255) REFERENCES market.instagram(id),
    hashtag_index int REFERENCES market.instagram_hashtag(index_num)
);
