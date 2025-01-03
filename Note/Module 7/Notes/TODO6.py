import requests

URL = 'http://164.68.107.70:6060/api/v1/CreateProduct'

PAYLOAD={
    "ProductName": "Rabbil Python",
    "ProductCode": "2113131",
    "Img": "abc",
    "UnitPrice": "12",
    "Qty": "1",
    "TotalPrice": "12"
}

HEADER = {
    "Content-Type": "application/json"
}

response = requests.post(url=URL,json=PAYLOAD,headers=HEADER)

statuscode = response.status_code
jsondata = response.json()
header = response.headers

print(statuscode)
print(jsondata)
print(header)
