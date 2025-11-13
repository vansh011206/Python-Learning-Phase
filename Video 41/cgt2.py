str = 'enumerate'
vowel = ['a','i','e','o','u']
for index,letter in enumerate(str):
    if (letter in vowel):
        print(index,letter)