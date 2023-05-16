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
    with open('TKH-Social-Media-Engagement-Analytics\sql\youtube_schema.sql', 'r') as schema:
        queries = schema.read()
        print(queries)
        cursor.execute(queries)




#youtube 
    with open('TKH-Social-Media-Engagement-Analytics\data\youtube_data.csv', 'r') as f:    
        cmd = 'COPY market.youtube (title, id, url, viewCount, date, likes, duration,commentsCount) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)

    conn.commit()