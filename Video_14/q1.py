num = []
for i in range(4):
    n = int(input("enter the Number :"))
    num.append(n)

print(num)

if num[0]>num[1] and num[0]>num[2] and num[0]>num[3]:
    print(f"The greatest of these four is {num[0]}")
elif num[1]>num[2] and num[1]>num[3]:
    print(f"The greatest of these four is {num[1]}")   
elif num[2]>num[3]:
    print(f"The greatest of these four is {num[2]}") 
else:
    print(f"The greatest of these four is {num[3]}")        



# num = []
# for i in range(4):
#     n = int(input("Enter the Number: "))
#     num.append(n)

# print(f"The greatest of these four is {max(num)}")
