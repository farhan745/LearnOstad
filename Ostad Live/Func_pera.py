#Tuple Function
def addTwo(*num):
    print(num)
addTwo(50,100,150,200,250)
#dictionary Function
def addDictTwo(**person):
    for key,value in person.items():
        print(f"{key}: {value} ")

addDictTwo(
    name = "Farhan",
    age=22,
    city = "Bangladesh"
)