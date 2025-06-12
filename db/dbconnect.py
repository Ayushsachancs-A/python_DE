import sqlite3
import pandas as pd


#connect to db and create file
conn = sqlite3.connect('demo.db')
cursor=conn.cursor()

#create table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               grade TEXT
               )''')

#Insert sample data 
cursor.execute("INSERT INTO students(name,age,grade) VALUES (?,?,?)",("ram",25,"A"))
cursor.execute("INSERT INTO students(name,age,grade) VALUES (?,?,?)",("shyam",45,"C"))

#query data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

#print result
for row in rows:
    print(row)


#load to pandas
df=pd.read_sql_query("SELECT * FROM students",conn)
print(df)

