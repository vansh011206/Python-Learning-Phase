class person:
    def __init__(self,a1,a2):
        print('Ho raha h run')
        self.name = a1
        self.occ = a2
        print(f'the values are {self.name},{self.occ}')
    @halua.setter #ye lagate h jab yahn se dooosri value chaiye hoti h chnage karne ke liye
     
    def halua(self,new):
            self.halua =new
        
a = person(4,6)  
  
# b = person(8,7) 
a.halua = 45
print(a.halua)