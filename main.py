import psycopg2
import sys

## Define Database args.
#conn = psycopg2.connect(database="tipsdb", user="appexternal", password="123123", host="10.30.31.247", port="5432", sslmode='require')
conn = psycopg2.connect(database="insightdb", user="appexternal", password="123123", host="10.30.31.247", port="5432", sslmode='require')

## Defind SQL Query Command.
#postgreSQL_select_Query = "select * from tips_endpoints"
postgreSQL_select_Query = "select * from radius_acct where end_time is not null"

## Defind Connection.
cur = conn.cursor()

## Defind Execute Command via Connection.
cur.execute(postgreSQL_select_Query)

## Defind Database Return data as "records".
records = cur.fetchall()


## Print Data.
print(records)

## Save to CSV.
outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(postgreSQL_select_Query)
with open('resultsfile.csv', 'w') as file:
    cur.copy_expert(outputquery, file)

## Close Connections.
cur.close()
conn.close()
