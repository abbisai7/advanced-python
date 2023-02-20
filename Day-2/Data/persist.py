from datetime import date
import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, verify=False)
todos = json.loads(response.text)

#memory level serialization with json

data = json.dumps(todos,indent=2)
#print(data)


#file level serialization with json
with open('datafile.json','w') as writer:
    json.dump(data,writer)
    print("done")
 
#desearlize jsonf 
with open("datafile.json","r") as reader:
    data = json.load(reader)
    print(data)
