class person:
    def __init__(self,a1,a2):
        print('Ho raha h run')
        self.name = a1
        self.occ = a2
    def info(self):
        print(f'Kuch mat karo tum {self.name} bas {self.occ} karo') 
        
        
a = person('Vanshaj','Bakchodi')    
b = person('Sweta','Padhai')  
a.info()
b.info()    
        