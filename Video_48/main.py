x = 10

print( f' pehle {x}')

def func():
    global x
    x = 9
    y = 8
    print(f'locak variable is {y}')
    # print (f'function wala{x}')

func() 
print (f'function wala{x}')
