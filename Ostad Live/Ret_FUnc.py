def addTwo(a,b):
    num1 = a
    num2 = b
    return num1+num2
result = addTwo(20,10)
print(result)

def addTwostr(a,b):
    num1 = a
    num2 = b
    return {"sum": num1+num2}
result1 = addTwostr(20,10)
print(result1)

#Lambda function
result = lambda x,y: x+y
print(result(10,100))

def myFunc(n):
    return lambda x: x*n

resultFunc= myFunc(10)
print(resultFunc(22))