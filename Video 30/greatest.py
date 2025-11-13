def greatest(m,n,o):
    if m>o and m>n:
        return m
    elif n>o:
        return n
    else:
        return o
    
print('The Greatest of three numbers is ', greatest(12,34,43))   