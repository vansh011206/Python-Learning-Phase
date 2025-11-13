marks = []
for i in range(3):
    n = int(input("Enter the Number: "))
    marks.append(n)
# print(marks)

sum=0
for i in marks:
    sum = sum + i
print(sum)

total = 300
total_percentage = (sum/total)*100

if marks[0]>33 and marks[1]>33 and marks[2]>33 and total_percentage>=40:
    print("This student is pass")
else :
    print("This student is fail")    









# if all(mark >= 33 for mark in marks) and total_percentage >= 40:
#     print("This student has passed.")
# else:
#     print("This student has failed.")    
