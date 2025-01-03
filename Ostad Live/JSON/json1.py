import json
from xml.etree.ElementTree import indent
'''
#Python Object ---> JSON str
personOBJ = {
    "name":"Jon",
    "age":30,
    "city":"New york",
    "hasChildren":False,
    "title":["engineer","programmer"]
}
personJSon=json.dumps(personOBJ,indent=4)
print(personJSon)

# JSON str ---> Python Object
person_obj=json.loads(personJSon)
print(person_obj)

#Python Object ---> JSON str+file write
personOBJ = {
    "name":"Jon",
    "age":30,
    "city":"New york",
    "hasChildren":False,
    "title":["engineer","programmer"]
}
with open("person.json","w") as personJSONFile:
    json.dump(personOBJ,personJSONFile,indent=4)
'''
#JSON file read-> Python Obj->JSON str
with open ("person.json","r") as personOBJFile:
    obj=json.load(personOBJFile)
    print(obj)