# def square(x):
#     return x*x

# print(square(5))

def doub(fx,value):
    return 6 + fx(value)
    
    
square = lambda x:x*x

print(square(6))
print(doub(square,4))