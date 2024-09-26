# file = open("my_file2.txt","r")
# content = file.read()
# print(content)
# file.close()

# f = open("Shree.txt","r")
# line = f.readline()
# print(line)
# f.close()

# f = open("Shree.txt","r")
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()

file = open("Shree.txt","a")
file.write("\n this is some new content")
file.close()