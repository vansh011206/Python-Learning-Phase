class Microsoft:
    company = 'Microsoft'
    def __init__(self,name,designation):
        self.name = name
        self.post = designation
    def show(self):
        print(f'{self.name} is {self.post} in {self.company}')    

a = Microsoft('Vanshaj','SDE')    
b = Microsoft('Harry','SSDE')

c = Microsoft('Sahil','DEO')
# Microsoft.company = 'Google'
d = Microsoft('Ayush','JSDE')

a.show()
b.show()
c.show()
d.show()

        
    