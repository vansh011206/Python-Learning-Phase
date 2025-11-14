# file = open('file.txt','r')
# text = file.read()
# print(text)
# file.close()

# pyfile = open('nayi.txt','a')
# pyfile.write('Hello\n')
# pyfile.close()

for i in range(0,4):
    with open('file2.txt','a') as f:
        f.write(f'\nEk Nayi file{i+1}')