import requests
import json
url = "http://192.168.0.1"


data = [{'c': 'C', 'b':(1, 6), 'a': 'A'}]
json_data = json.dumps(data,sort_keys=True)
print(data)
print(json_data)

try:
    r=requests.post(url, json=json_data)
except:
    print("连接主机失败")
else:
    print(r.text)
