import pickle
import json,requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, verify=False)

data = json.loads(response.text)

with open("report.p","wb") as fh:
    pickle.dump(data,fh)
    print("Done")

with open("report.p","rb") as fh:
    data = pickle.load(fh)
    print(data)


