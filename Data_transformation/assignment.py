import pandas as pd
df=pd.read_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\pythonDE\Data_transformation\sales_data.csv")



# Filter: All rows where status == 'Completed'
s=df[df['status'] =='Completed']
print(s)







# Group: Total sales amount per region
ts=df.groupby('region')['amount'].sum().reset_index()
print(ts)




# Add Column: final_amount = amount + tax
df['tax']=df['amount']*0.18
df['final_amount']= df['amount'] + (df['amount']*0.18)
print(df)



# Join: Add city info using merge
city=pd.DataFrame({
    "customer":['Alice','Bob','Charlie'],
    "city":["noida","Delhi","Ghaziabad"]
})

merged_df= pd.merge(df,city,on='customer',how='left')
print(merged_df)


# Export: Save final result to final_output.csv
merged_df.to_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\pythonDE\Data_transformation\output.csv",index=False)


# "How do you group data by X and get sum/count/avg?"
df.groupby("region")["amount"].agg(["sum", "mean", "count"])