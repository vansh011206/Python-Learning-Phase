l = [1,32,3,43,23]


from functools import reduce

mul = reduce(lambda x,y:x*y , l )
print(mul)