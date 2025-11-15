class this:
    def __init__(self):
        self.name = 'Vanshaj'
    
    def __ok(self,n):
        print(f'Dear {n} this function is private becuase of double underscore')
a = this()
print(a.name)    
# a.__ok('harry') #cannnot access

a._this__ok('Harry') #this will run