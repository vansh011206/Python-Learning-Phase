# Divide two numbers and handle divide-by-zero error.

try:
    a = int(input('Enter a number : '))
    b = int(input('Enter a number : '))
    print(a/b)
except ZeroDivisionError :
    print('Cannot be divide by zero')    
except ValueError:
    print('Invalid input.. Please enter a number')    