# for getter and setter

class hr:
    def __init__(self,age,name):
        self._name = name
        self._age = age
        
    def get_age(self):
        return self._age
    
    def get_name(self):
        return self._name
    
    def set_age(self,age):
        if age>0:
            self._age = age
        else:
            print('Age is only positive number')  
     
    def set_name(self,name):
        self._name = name
        
a = hr(19,'Vanshaj')        
        
# a.set_age(-5)  
a.set_name('halwa')    
print(a.get_name())          
       