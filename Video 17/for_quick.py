l = [1,2,4,3,2]
for item in l:
    print(item*item)

# break statement
for i in l :
    print (i/2) 
    if i==4:
        break
    else:
        print("everything is fine till now")  

for i in l :
    
    if i==4:
        continue
    print (i/2) 
     