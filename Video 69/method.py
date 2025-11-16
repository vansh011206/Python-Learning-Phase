class Identity:
    company = 'Apple'
    def showname(self):
        print(f'Your name is {self.name} and You work in {self.company}')
    @classmethod
    def changename(cls): #@classmethod is used to change the variables of the class directly
        # cls.name = changedname
        return cls
        
        
        
a = Identity()
a.name = 'Vanshaj'
a.showname()        
print(a.changename())