# num = int(input('Enter the number'))

# l = [2,3,5,7]

# if num in l:
#     print(f'{num} is prime number')
# elif all(num%item==0 for item in l) and num%num==0:
#     print(f'{num} is prime number')
# else:
#     print(f'{num} is not prime number')    


num = int(input("Enter the number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
