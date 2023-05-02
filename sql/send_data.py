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
    conn.commit()

    
'''
    # (PART OF) SPRINT 6
    # DUE UNTIL 5/10 (WEDNESDAY OF NEXT WEEK)
    with open('phase_3/week_7/data/customers.csv', 'r') as f:    
        cmd = 'COPY store.customer(cust_id, fname, lname, account_create) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
    conn.commit()
'''
    
