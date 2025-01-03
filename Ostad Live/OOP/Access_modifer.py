'''
1.Public
2.Protected
3.Private
'''
'''
#public
print("Public:")
class car:
    brand = "Toyota"
    def show(self):
        print(f"Brand name is: {self.brand}")
class sedan(car):
    def showFromchild(self):
        print(f"Our Brand: {self.brand}")

obj = sedan()
print(obj.brand)
obj.showFromchild()

#protected
print("Protected:")
class car:
    _brand = "Toyota"
    def show(self):
        print(f"Brand name is: {self._brand}")
class sedan(car):
    def showFromchild(self):
        print(f"Our Brand: {self._brand}")

obj = sedan()
print(obj._brand)
obj.showFromchild()
'''
#private
print("Private:")
class car:
    __brand = "Toyota"
    def show(self):
        print(f"Brand name is: {self.__brand}")
class sedan(car):
    def showFromchild(self):
        print(f"Our Brand: {self.__brand}")

obj = car()
obj.show()