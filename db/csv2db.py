import pandas as pd
import sqlite3



#read csv to DataFrame
df=pd.read_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\pythonDE\db\students.csv")
print(df)


#connect sqlite
conn= sqlite3.connect('school.db')


#Insert dataframe into DB table
df.to_sql('students',conn,if_exists='replace',index=False)


#read from DB
results= pd.read_sql_query("SELECT * FROM students",conn)
print(results)


#query on db and store as csv
age=pd.read_sql_query("SELECT id,name,age FROM students WHERE age>21",conn)
age.to_csv("ar.csv",index=False)

conn.close()