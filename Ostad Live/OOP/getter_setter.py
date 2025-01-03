'''
class car :
    __brand = "toyota"
    def brand(self):
        return self.__brand

obj = car()
print(obj.brand())
'''
#Getter
print("\nGetter:")
class car :
    __brand = "Bugati"
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,value):
        print("After Setter")
        self.__brand=value


obj = car()

print(f"Brand Name: {obj.brand}")

#Setter
class carSetter :
    __brand = "Bugati"
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,value):
        print("After Setter:")
        self.__brand=value


obj = carSetter()
obj.brand="Mazda"
print(f"Brand Name: {obj.brand}")