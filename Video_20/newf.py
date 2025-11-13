# average of n number
def avearge(*numbers):
    sum = 0
    for i in numbers:
      sum = sum + i 
    print("The Average is",sum/len(numbers) )

avearge(2,3,4,2,4,23,3,43,2,2,3)    