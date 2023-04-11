import csv 
import sqlite3
import pandas as pd

connection = sqlite3.connect('store.db')

# creating a  cursor object to execute sql queries on a database table
cursor = connection.cursor()

# defining table
create_table = '''CREATE TABLE IF NOT EXISTS ddmmyyy_verge(
                    ID INTEGER PRIMARY KEY,
                    URL TEXT,
                    HEADLINE TEXT,
                    AUTHOR TEXT,
                    DATE TEXT
                    );'''

# add this table to our database using cursor object
cursor.execute(create_table)

# lets open the csv file
file = open('temp.csv')

contents = csv.reader(file)
# print(list(contents))
# query to insert data in table
insert_records = "INSERT OR IGNORE INTO ddmmyyy_verge(ID, URL, HEADLINE, AUTHOR, DATE) VALUES(?,?,?,?,?)"
# importing the content of our csv file to this table
cursor.executemany(insert_records, contents)

# crosschecking by printing data from sqlite database table
# data = "SELECT * FROM ddmmyyy_verge"
# rows = cursor.execute(data).fetchall()
# for r in rows:
#     print(r)
connection.commit()
connection.close()
# import os
# file = 'temp.csv'
# if(os.path.exists(file) and os.path.isfile(file)):
#     os.remove(file)
# os.close("temp.csv")