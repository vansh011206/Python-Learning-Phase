num = int(input('Enter a number'))
if num>5 or num<0:
    raise ValueError('Enter num between 0 and 5')