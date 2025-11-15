l = [1,32,3,43,23]
square = lambda x:x*x 
ans = list(map(square,l))

print(ans)


def greater(a):
    return a>35

print(list(filter(greater,l)))