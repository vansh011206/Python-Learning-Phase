import math

class Calculator:
    def __init__(self,num):
        self.num = int(num)
    def sqaure(self):
        return self.num*self.num
    def cube(self):
        return self.num*self.num*self.num
    def sqroot(self):
        return math.sqrt(self.num)
    
    
    
a = Calculator(20)
print(f'The sqaure of {a.num} is {a.sqaure()}')
print(f'The cube of {a.num} is {a.cube()}')
print(f'The Sqaure root of {a.num} is {a.sqroot()}')
    
