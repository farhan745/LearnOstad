import requests

URL = 'http://164.68.107.70:6060/api/v1/ReadProduct'
response = requests.get(URL)
statuscode = response.status_code
jsondata = response.json()
header = response.headers

print(statuscode)
print(jsondata)
print(header)