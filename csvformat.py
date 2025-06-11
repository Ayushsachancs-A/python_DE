import csv

#Read Csv
with open("new.csv",mode='r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

    



#write a csv file
data=[["name","age"],["Alice",30],["bob",25]]
with open("new.csv",mode='w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(data)

#using pandas
import pandas as pd

# #read
df=pd.read_csv('new.csv')
print(df.head())

#write
df.to_csv("output.csv",index=False)

 
#Assignment to Filter the rows where pm25 > 100.
import pandas as pd
df=pd.read_csv('aq.csv')
print("Original Data")
print(df)


print("filter data")
newdata= df[df['pm25']>100]
print(newdata)

print("new File")
newdata.to_csv("filter.csv",index=False)





