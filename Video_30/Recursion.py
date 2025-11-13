def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

user =int(input("Enter the number: "))
print(f"The Factorial of this number is : {factorial(user)} ")
