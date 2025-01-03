#Request Payload
import requests
import json
URL = 'http://164.68.107.70:6060/api/v1/CreateProduct'
PAYLOAD = {
    "ProductName":"Farhan",
    "ProductCode":"2113131",
    "Img":"abc",
    "UnitPrice":"30",
    "Qty":"2",
    "TotalPrice":"20",
    "Gender":"Male"
}

HEADER = {
  'Content-Type': 'application/json'
}
responce=requests.post(url=URL,json=PAYLOAD,headers=HEADER)
statusCode = responce.status_code
print(statusCode)
JSON = responce.json()
print(f'Json Data: {JSON}')
header = responce.headers
print(f'Header: {header}')


