    def get_name(self):
        return self._name
    
    def set_age(self,age):
        if age>0:
            self._age = age
        else:
            print('Age is only positive number')  
     
    def set_name(self,name):
        self.name = name
        
a = hr(19,'Vanshaj')        
        
# a.set_age(-5)  
print(a.set_name('halwa')    