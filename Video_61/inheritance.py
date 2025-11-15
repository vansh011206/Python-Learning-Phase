# Inheritence h ye 


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
        print(f'The name of employee {self.id} is {self.name}')  

# iski properties niche wali m jaaegi        
        
class doosriwali(Employee):
    def lang(self):
        print(f'The most used language of employee {self.id} {self.name} is python') 

# isme bhi niche jaegi properties        
        
class teesriwali(doosriwali):
    def address(self):
        print(f'Employee code {self.id} jiska naam {self.name} h vo Faridabad m rehta h ')             
# a = Employee('haua',69)     
# a.show()     

# doosri = doosriwali('haanji',89)
# doosri.lang()


t = teesriwali('Vanshaj',69)
t.address()