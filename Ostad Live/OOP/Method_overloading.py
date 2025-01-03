class father :
    x = 10
    y = 20
    def addtwo(self,a=0,b=0):
        print(self.x+self.y+a+b)
    def mymethod(self,*a):
        print(a)

obj = father()
obj.addtwo()
obj.addtwo(10)
obj.addtwo(10,20)


obj.mymethod(1)
obj.mymethod(1,2)
obj.mymethod(1,2,3)