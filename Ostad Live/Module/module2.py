import http.client

conn=http.client.HTTPSConnection("rabbil.com")
conn.request("GET",'/')
response = conn.getresponse()
print(response.status)
print(response.headers)
print(response.read())
