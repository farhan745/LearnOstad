"""
class father():
    x =  10
    y = 20
    print("i am Father")
    @staticmethod
    def addtwoFather():
        return (father.x+father.y)

class son(father):
    print("i am son")

    def addtwo(self):
        fatherCome = self.addtwoFather()+100
        print(fatherCome)
        print(f"Hello {self.x} & {self.y}")

son().addtwo()
#father().addtwo()
"""
#If Child has static properties, Parent can't access as it is like child
"""
class Father:
 pass
class Son(Father):
 a = 10
 b = 20

 @staticmethod
 def addtwo():
    print(Son.a + Son.b)

Son.addtwo()
Father.addtwo()

print(Son.a)
print(Son.b)
"""
#How child can access parents static and non-static properties
'''
class Father:
 a = 10
 b = 20

 @staticmethod
 def addtwo():
    print(Father.a + Father.b)


 def addthree(self):
    print(self.a + self.b+10)


class Son(Father):

 def addnew(self):
    self.addthree()
    Father.addtwo()


obj = Son()
obj.addnew()
'''

#Child can override parent method
'''
class Father:
    num1 = 0
    num2 = 0
    def addTwo(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2
class Son(Father):
 def addTwo(self, num1, num2):
 # Overriding the method
    print(f"Adding {num1} and {num2} in Son")
    return num1 + num2 + 1 # Modified behavior
# Creating instances of Father and Son
father = Father()
son = Son()
# Calling the addTwo method from Father and Son
print(father.addTwo(5, 3)) # Output: 8
print(son.addTwo(5, 3)) # Output: Adding 5 and 3 in Son
'''
