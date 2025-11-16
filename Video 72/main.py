class name:
    def __init__(self,name):
        self.name=name
        
    def printname(self):
        print('Vanshaj,Mansha')

class age(name):
    def printage(self):
        print('Both are of same age i.e, 19') 
    super().__init__(name) 
  

a = age('harry')
# a.printage()
# a.printname()
print(a.name)              
              