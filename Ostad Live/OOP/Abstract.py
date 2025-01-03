from abc import ABC,abstractmethod
class Bangladesh(ABC):
    @abstractmethod
    def print0to10(self):
        pass
    def print10to20(self):
        for i in range(10,20):
             print(i)
class Dhaka(Bangladesh):
    def print0to10(self):
        pass
obj = Dhaka()
obj.print10to20()
