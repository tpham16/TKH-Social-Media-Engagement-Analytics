import psycopg2
import psycopg2.extras
import csv
import os



my_password = os.environ.get('password') 

# aws rds 
params = {
    "host"      : "rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  : my_password,
    "port" : "5432"
}

conn = psycopg2.connect(**params)

with conn.cursor() as cursor:
    with open('sql/schema.sql', 'r') as schema:
        queries = schema.read()
        print(queries)
        cursor.execute(queries)
    
    # twitter
    with open('data/tweets.csv', 'r', encoding = 'cp850') as f:    
        cmd = 'COPY market.twitter FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)


    # youtube
    with open('data/youtube_data.csv', 'r',encoding = 'cp850') as f:    
        cmd = 'COPY market.youtube  FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)

    # instagram 
    with open('data/ig_without_hashtags.csv', 'r',encoding = 'cp850') as f:    
        cmd = 'COPY market.instagram FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)

    with open('data/ig_just_hashtags.csv', 'r',encoding = 'cp850') as f:    
        cmd = 'COPY market.instagram_hashtag FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)

    with open('data/IG_primary_table.csv', 'r',encoding = 'cp850') as f:    
        cmd = 'COPY market.instagram_hash_post FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)

    conn.commit()