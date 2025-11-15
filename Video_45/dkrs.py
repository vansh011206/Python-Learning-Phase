import os 
# os.makedirs("Projects/Python/Day1")
# os.remove('tempCodeRunnerFile.py')
# os.remove('Projects')
import shutil
shutil.rmtree("Projects")
if os.path.exists("myfile.txt"):
    print("File exists")
else:
    print("No such file")
