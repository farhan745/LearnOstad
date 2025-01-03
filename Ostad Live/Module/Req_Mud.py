import requests
URL='http://164.68.107.70:6060/api/v1/ReadProduct'
responce = requests.get(URL)
status_code = responce.status_code
jsonData = responce.json()
print(status_code)
print(jsonData)
header = responce.headers
print(f"Header: {header}")