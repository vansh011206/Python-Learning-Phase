num = int(input('Enter the number'))

l = [2,3,5,7]

if all(num%item==0 for item in l) and num%num==0:
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')    