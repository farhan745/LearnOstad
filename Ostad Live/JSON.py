#JSON
import json
from xml.etree.ElementTree import indent

bill ={
    "name":"Bills Gate",
    "Age": 70,
    "Country":"USA"
}
billJSON = json.dumps(bill,indent=4)
print("JSON is: ",(billJSON))