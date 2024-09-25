# Student List
student_list1 = ["Alok", "Pavan", "arjun", "Sharat"]

# List operations

print("\nThe list of students is:\n", student_list1)  

student_list1.append("Pragyananda") 
print("\nThe append operation\n", student_list1)

student_list1.insert(2, "Rakesh")
print("\nThe insert operation at 2nd position\n", student_list1) 

student_list2 = ["Ramya", "Reema"]

student_list3 = student_list1 + student_list2 
print("\nThis is list_addition example\n", student_list3)

# Nested list example

nested_student_list = [student_list1, student_list2, student_list3]
print("\nNested list example\n", nested_student_list)
print("\nThe list at position 2 is:\n", nested_student_list[2])

# List operations

print("\nLength of nested list is:\n", len(nested_student_list))  
print("\nMax of nested list is:\n", max(nested_student_list))
print("\nMin of nested list is:\n", min(nested_student_list))  

# Additional list operations

student_list4 = ["Bharat", "Ramesh", "Suresh", "Veer", "Seema", "Mary"]
print(student_list4.count(4))  
print(student_list4.index("Suresh"))
student_list4.reverse()
print("\n", student_list4, "\n")
student_list5 = student_list4.extend(student_list3)
print(student_list5)

print("\n\n======================================================\n\n")

# Student Tuple
student_tuple1 = ("Alok", "Pavan", "Madhvi", "Sharat")

# Tuple operations

print("\nThe tuple of students is:\n", student_tuple1)  

student_tuple1 = student_tuple1 + ("Pragyananda",)
print("\nThe append operation\n", student_tuple1)

student_tuple1 = student_tuple1[:2] + ("Rakesh",) + student_tuple1[2:]  
print("\nThe insert operation at 2nd position\n", student_tuple1)

student_tuple2 = ("Ramya", "Reema")

# Tuple addition (concatenation)
student_tuple3 = student_tuple1 + student_tuple2
print("\nThis is tuple_addition example\n", student_tuple3)

# Nested tuple example
nested_student_tuple = (student_tuple1, student_tuple2, student_tuple3)
print("\nNested tuple example\n", nested_student_tuple)
print("\nThe tuple at position 2 is:\n", nested_student_tuple[2])

# Tuple operations
print("\nLength of nested tuple is:\n", len(nested_student_tuple)) 
print("\nMax of nested tuple is:\n", max(nested_student_tuple))  
print("\nMin of nested tuple is:\n", min(nested_student_tuple)) 

# Additional tuple operations
student_tuple4 = ("Bharat", "Ramesh", "Suresh", "Veer", "Seema", "Mary")
print(student_tuple4.index("Suresh")) 

print("\n\n======================================================\n\n")

# Student Set
student_set1 = {"Alok", "Pavan", "arjun", "Sharat"}

# Set operations

print("\nThe set of students is:\n", student_set1) 

student_set1.add("Pragyananda") 
print("\nThe add operation\n", student_set1)

student_set2 = {"Ramya", "Reema"}

# Set union
student_set3 = student_set1.union(student_set2)
print("\nThis is set_union example\n", student_set3)

# Set operations
print("\nLength of set is:\n", len(student_set3)) 

# Additional set operations
student_set4 = {"Bharat", "Ramesh", "Suresh", "Veer", "Seema", "Mary"}

# Union operation
student_set5 = student_set4.union(student_set3)
print("\nThis is union operation\n", student_set5)

# Intersection operation
student_intersection = student_set5.intersection(student_list4)
print("\nThis is intersection operation\n", student_intersection)

student_diff = student_set5.difference(student_set4)
print("\nThis is difference operation\n", student_diff)

print("\n\n=======================")

student_info = {'name': 'Sharat', 'age': 20, 'branch': 'CSE'}
print("The student info is:\n", student_info)
print("\nThe type of input is:\n", type(student_info))

student_info['year'] = '3rd Year'
print("\nThe new student info is:\n", student_info)

student_info['projects'] = ['AI', 'ML', 'Cybersecurity']
print("\nThe student's projects added are:\n", student_info)

# Accessing the info
student_info['projects']  
student_info.get('branch')

# Value updating
student_info['age'] = 21
print('Updated info')
print(student_info)

print("\nThe items in the student info are:\n", student_info.items())

print("\nThe keys in the student info are:\n", student_info.keys())

print("\nThe values in the student info are:\n", student_info.values())
