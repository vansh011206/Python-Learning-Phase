a = "Vanshaj Sharma"
print(len(a))
# print(a[7])
print(a.endswith("ma"))
print(a.startswith("V"))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.title()) #har word ka first letter capital
print(a.strip()) #extra spaces hata deta h
print(a.replace("Vanshaj","Unknown"))
print(a.count("a")) # Kitni baar koi character ya word repeat hua hai – wo batata hai.
print(a.split()) #String ko tod deta hai list mein (default: space pe).
print(a.isalpha())
print("abc".isalpha())  # True
print("123".isdigit())  # True
print("abc123".isalnum())  # True

