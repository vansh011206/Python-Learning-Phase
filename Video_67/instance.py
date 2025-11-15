class this:
    Girlfrindname = 'Meghna'         #Class associated variables  sab ke liye same hongi
    
    #instance associated variables sab ke liye alag
    def __init__(self,name):
        self.name = name
    
    def ok(self):
        print(f'Dear {self.name} Your Girfriend name is {self.Girlfrindname}')
        
a = this('Vanshaj')

a.ok()
a.Girlfrindname = 'Hakina'
a.name = 'Hakka'
a.ok()
