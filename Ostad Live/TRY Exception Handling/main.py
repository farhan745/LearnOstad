x=10 
y =0
try:
   z = x/y
   print(z)
except ZeroDivisionError:
  print(ZeroDivisionError)

a= "Hello"
b=5
try:
   c = a+b
   print(c)
except TypeError as e:
  print(e)