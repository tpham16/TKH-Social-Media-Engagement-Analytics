CREATE OR REPLACE FUNCTION market.max_youtube_inter() RETURNS RECORD AS $$
	DECLARE 
		VAL RECORD;
	BEGIN
		select title, date
		from market.youtube
		where likes in(
			select max(likes)
			from market.youtube)
		INTO VAL;
		RETURN VAL;
	END $$




CREATE OR REPLACE FUNCTION market.total_interactions() RETURNS TABLE(
platform VARCHAR, total_likes FLOAT) AS $$
	BEGIN
		RETURN QUERY
		SELECT likes_total.platform::varchar(8), likes_total.total_likes::float
		FROM (
			SELECT 'Youtube' as platform, AVG(likes) AS total_likes
			FROM market.youtube
			UNION ALL
			SELECT 'Instagram' as platform, AVG(likescount) AS total_likes
			FROM market.instagram
			UNION ALL
			SELECT 'Twitter' as platform, AVG(likes) AS total_likes
			FROM market.twitter
			) AS likes_total;
	END $$
LANGUAGE plpgsql;