class number:
    name = 'Vanshaj'
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
        
    
a = number()
print(a.name) 
print(len(a))   