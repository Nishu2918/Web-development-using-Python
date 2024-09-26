try:
    file = open("Nishanth.txt","x")
except FileExistsError:
    print("File already exits!")


        