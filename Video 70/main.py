class Employee:
    def __init__(self,name,age,gender):
        self.name = name
        self.gen = gender
        self.age = age
    @classmethod
    def change(cls,str):
          name , age , gender = str.split('-')
          return cls(name,int(age),gender)

    
# a = Employee('Vanshaj','19','Male')
# print(a.age)
# print(a.gen)
# print(a.name)

str = "Vanshaj-19-Male"

# b = Employee.change(str)
# print(b.name)
# print(b.age)
# print(b.gen)

c = Employee.change(str)
print(c.name)
print(c.age)
print(c.gen)