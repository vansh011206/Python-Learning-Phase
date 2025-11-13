try:
    l = [1, 2, 3]
    print(l[5])
except IndexError as e:
    print("Error Occurred:", e)
