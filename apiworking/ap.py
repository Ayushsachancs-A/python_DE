#way to request api
import requests 
#to turn json data into Dataframe(table) and save to csv
import pandas as pd

#Defien api url with query paramters
url="https://api.coingecko.com/api/v3/coins/markets"

#dict to hold query parameters that api expects like convert to usd,get coins only top 10
#sort coin by market cap desc
param={
    "vs_currency":"usd",
    "order":"market_cap_desc",
    "per_page":10,
    "page":1,
    "sparkline":"false"
    }

#make get Requests
response= requests.get(url,params=param)


#check response status
if response.status_code == 200:
    data = response.json()
else:
    print("ERROR:", response.status_code)
    exit()

#flatten and normalise the data
coins=[]
for coin in data:
        coins.append({
            "name":coin["name"],
            "symbol":coin["symbol"],
            "price":coin["current_price"],
            "market_cap":coin["market_cap"],
            "volume": coin["total_volume"],
            "24h_change": coin["price_change_percentage_24h"]
        })

#convert to dataframe to save
df=pd.DataFrame(coins)
print(df.head())

#save to csv
df.to_csv("crypto.csv",index=False)


