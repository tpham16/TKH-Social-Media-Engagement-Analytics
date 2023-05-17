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


SELECT market.max_youtube_inter()

CREATE OR REPLACE FUNCTION market.name_of_function() RETURNS RECORD AS $$
	DECLARE 
		VAL RECORD;
	BEGIN
		select id, date
		from market.youtube
		where likes in(
			select max(likes)
			from market.youtube)
		INTO VAL;
		RETURN VAL;
	END $$


SELECT market.max_youtube_inter()
LANGUAGE plpgsql;