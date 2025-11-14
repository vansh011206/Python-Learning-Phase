# Given a list of people with their age, filter out only adults and get their names in uppercase:

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 15},
    {"name": "Eve", "age": 19},
    {"name": "Meena", "age": 22},
    {"name": "Rahul", "age": 16},
    {"name": "Sita", "age": 18},
    {"name": "Ravi", "age": 21},
    {"name": "Anu", "age": 14},
    {"name": "Mohit", "age": 45},
    {"name": "Rina", "age": 32},
    {"name": "Karan", "age": 12},
    {"name": "Tina", "age": 20},
    {"name": "Kabir", "age": 17},
    {"name": "Alex", "age": 28},
    {"name": "Nina", "age": 13},
    {"name": "Zoya", "age": 19},
    {"name": "Jai", "age": 23},
    {"name": "Ishaan", "age": 16}
]

from functools import reduce

adults = list(filter(lambda person: person["age"] >= 18, people))
adult_names_upper = list(map(lambda person: person["name"].upper(), adults))

print("Adults' Names in Uppercase:")
print(adult_names_upper)

        
