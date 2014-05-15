from.import requests
import json

data = {
    "startTime": "2014-05-08",
    "src": None,
    "password": None,
    "pageNum": "1",
    "name": None,
    "limitNum": "20",
    "endTime": "2014-05-15",
    "dst": None,
    "callCenterIds": "32"
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json"
}
url = "http://ccapi.xdf.cn/cc/SalesforceCron/getTelCallLogInfo"
res = requests.post(url, json.dumps(data), verify = False, headers = headers, timeout = 120)
print(res.json())
