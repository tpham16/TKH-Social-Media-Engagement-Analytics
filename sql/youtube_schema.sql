DROP TABLE IF EXISTS market.youtube;

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