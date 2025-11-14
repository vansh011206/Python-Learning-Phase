with open('file.txt','r') as f:
    f.seek(20)
    
    data = f.read(6)
    print(data)
    