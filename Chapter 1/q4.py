import os

# Specify the path (you can also use '.' for the current directory)
path = '/Windows'  # current directory

try:
    # Get the list of all files and directories
    contents = os.listdir(path)

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")