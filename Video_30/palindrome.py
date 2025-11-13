def palindrome(str,start,end):
    if (start!=end):
        return False
    elif(start>=end):
        return True
    else:
        return palindrome(str,start+1,end-1)
    
name = "lololololol"
print(palindrome(name,0,len(name)-1))
