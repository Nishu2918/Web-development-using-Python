import os
if os.path.exists("C:/Users/nisha/OneDrive/Desktop/Python web developer/Day 4 (Django)/demo.txt"):
    os.remove("C:/Users/nisha/OneDrive/Desktop/Python web developer/Day 4 (Django)/demo.txt")
    print("File deleted")
else:
    print("file does not deleted")                  