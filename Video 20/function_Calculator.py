def addition(a,b):
    add=a+b
    print(add)

def subtraction(a,b):
    sub=a-b
    print(sub)    

def multiplication(a,b):
    mul=a*b
    print(mul)

def divison(a,b):        
    div=a/b
    print(div)

num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number:"))
operator = input("Enter Operation(eg.+,-,*,/):")

if(operator=="+"):
    addition(num1,num2)
elif(operator=="-"):
    subtraction(num1,num2)
elif(operator=="*"):
    multiplication(num1,num2)  
elif(operator=="/"):
    divison(num1,num2)      
else:
    print("Incorrect Input")    
