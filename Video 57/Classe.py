class Person:   #classes
    name = 'vanshaj'
    stream = 'Science'
    Health = 'Good'
    def info(s):
        print(f'{s.name} is a {s.Health} {s.stream} Student')
    
a = Person()    #object
b = Person()
a.name = 'Sweta'
b.name = 'khushi'
print(a.name)
a.info()
b.info()


# s mtlb jispe ye method call hora h 