import pandas as pd


#read File
df=pd.read_csv(r'C:\Users\imean\OneDrive\Desktop\projecttss\pythonDE\Data_transformation\sales_data.csv')

print(df)


#filter based on sales
sales=df[df["amount"]>=200]
print(sales)


#print pereticular colums
print(df[["customer","region","amount"]])


# Add a column
df["tax"]=df["amount"]*0.18
print(df[["amount","tax"]])


#Handle missing values
df.isna().sum()
df.fillna(0,inplace=True)

#rename a colums
df.rename(columns={"amount":"order_amount"},inplace=True)
print(df)

#group by
grouped=df.groupby("customer")["order_amount"].sum().reset_index()
print(grouped)


#apply custom function
df["status_falg"]=df["status"].apply(lambda x: 1 if x=="Completed" else 0)
print(df)


#merge two dataframes
customer_info=pd.DataFrame({
    "customer":["Alice","Bob","Charlie"],
    "City":["Mumbai","Banglore","Kanpur"]

})

merge_df= pd.merge(df,customer_info,on="customer",how="left")
print(merge_df)




#save output
df.to_csv("transformed.csv",index=False)





