import os
if os.path.exists("Shree.txt"):
    os.rename("Shree.txt","Shreeram.txt")
    print("File renamed.")
else:
    print("The File does not exist.")