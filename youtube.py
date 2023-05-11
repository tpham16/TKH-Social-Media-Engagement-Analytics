import psycopg2
import psycopg2.extras
import csv
import os

params = {
    "host"      : "rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  : "ds2022_aws",
    "port" : "5432"     
}

conn = psycopg2.connect(**params)

with conn.cursor() as cursor:
    with open('TKH-Social-Media-Engagement-Analytics\sql\schema.sql', 'r') as schema:
        # read --> reads in entire file
        queries = schema.read()
        print(queries)
        # we are starting a transaction (or continuing)
        cursor.execute(queries)
    # commit your changes
    conn.commit()

    # (PART OF) SPRINT 6
    # DUE UNTIL 5/10 (WEDNESDAY OF NEXT WEEK)
    with open('TKH-Social-Media-Engagement-Analytics\data\youtube_data.csv', 'r') as f:    
        cmd = 'COPY market.youtube FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
    conn.commit()