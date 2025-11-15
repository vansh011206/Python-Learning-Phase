import datetime

now = datetime.datetime.now()
print(now)                 # Current date and time
print(now.year)            # Year
print(now.strftime("%A"))  # Day name like Monday