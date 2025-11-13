letters = ["a", "b", "c", "a", "d", "b"]
# Output:
# 'a' found at index 0 and 3
# 'b' found at index 1 and 5

# for index,letter in enumerate(letters):
#     if letter in letters:
#        next =  letters.index(letter,(index +1),len(letters))
#        if next:
#                print(f'{letter} found at {index} and {next}')


checked = []
for index,letter in enumerate(letters):
    if letter not in checked:
        indexes = [i for i,l in enumerate(letters) if l == letter]:
        if len(indexes)>1:
            print(f'{letter} found at {index} and {next}')
            
            