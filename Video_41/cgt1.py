colors = ["red", "blue", "green", "yellow", "pink", "black"]
# Output should be:
# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


for index,color in enumerate(colors):
    if index % 2 ==0:
        colors[index] = 'Even'
    else:
        colors[index] = 'Odd'   
        
print(colors)

# colors = ["red", "blue", "green", "yellow", "pink", "black"]

# for index, color in enumerate(colors):
#     if index % 2 == 0:
#         colors[index] = 'Even'
#     else:
#         colors[index] = 'Odd'

# print(colors)
        