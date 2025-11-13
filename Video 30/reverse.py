# reverse a string
def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:len(str)]) + str[0]
    

name = "vanshaj"   
print(reverse(name)) 