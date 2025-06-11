import json
#path handling
from pathlib import Path

print(Path.cwd())



# read
with open("data.json","r") as f:
    data=json.load(f)
    print(data)




#write in json
data={"name":"Ayush","age":20,"gender":"male"}
with open("data.json","w") as f:
    json.dump(data,f,indent=2)




#Assignment to save jason data on csv based on field like id,name,email,profile.location,profile.joined
import json
import pandas as pd
with open("user_data.json","r") as f:
    data=json.load(f)


#manual way
flat=[]
for u in data:
    fl={
        "id":u["id"],
        "name":u["name"],
        "email":u["email"],
        "location":u["profile"]["location"],
        "joined":u["profile"]["joined"]
    }
    flat.append(fl)
df= pd.DataFrame(flat)



#sortcut
df = pd.json_normalize(data, sep='_')




df.to_csv("jsondata.csv",index=False)











