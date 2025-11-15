# Square all even numbers from a list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = list(filter(lambda x : x%2==0,numbers))

# square = list(map(lambda x:x*x , new))
# print(square)


# Filter names that start with a vowel
# names = ["Ankit", "Rahul", "Esha", "Ishita", "Om", "Sanjay", "Uday"]
# vowels = ['a', 'e', 'i', 'o', 'u']

# def starts_with_vowel(name):
#     return name[0].lower() in vowels

# filtered_names = list(filter(starts_with_vowel, names))
# print(filtered_names)



# Create a list of cubes of numbers which are divisible by 3
nums = list(range(1, 21))

fileterd = list(filter(lambda x : x % 3 == 0 , nums))

cube = list(map(lambda c : c*c*c , fileterd))

print(cube)
