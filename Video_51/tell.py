i = 0
while True:
    with open('file.txt','r') as f:
        data = f.read(4)
        print(data)
        if not data:
            break
        i = i+1
        t = f.tell()
        f.seek(t)
    