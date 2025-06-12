import requests
import pandas as pd
import sqlite3


#call api
url="https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": False
}
response=requests.get(url,params=params)

if response.status_code !=200:
    print("Error:",response.status_code)
    exit()

data = response.json()


#extract Fields
coin=[]
for c in data:
    coin.append({
        "id":c["id"],
        "symbol": c["symbol"],
        "name":c["name"],
        "current_price":c["current_price"],
        "market_cap": c["market_cap"],
        "price_change_24" :c["price_change_24h"]
    })

df=pd.DataFrame(coin)
print(df)

#store in db
conn= sqlite3.connect("crypt.db")
df.to_sql("coin",conn,if_exists="replace",index=False)

#query
result= pd.read_sql_query("SELECT name,symbol,current_price FROM coin WHERE current_price>1000 ORDER BY current_price DESC",conn)
print(result)

conn.close()