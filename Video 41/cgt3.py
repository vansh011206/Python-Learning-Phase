numbers = [10, 3, 6, 8, 9, 12, 15]
ind = []
for index,num in enumerate(numbers):
    if num % 3 == 0:
        ind.append(index)
        
        
print(ind)        