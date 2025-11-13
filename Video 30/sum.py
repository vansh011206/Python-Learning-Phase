def sumofn(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + sumofn(n-1)
num = int(input("Enter any number :"))
print(f"The sum of {num} natural numbers is : {sumofn(num)}")