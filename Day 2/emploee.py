#employee
emp_list1 = ["sumit","shree","nishanth","keerthikumar"]

#list_operations

print("\nThe list of employees is:\n",emp_list1)    

emp_list1.append("amar")         
print("\nthe append opertion\n",emp_list1)

emp_list1.insert(2,"akbar")
print("\nthe insert operation at 2nd position\n",emp_list1) 

emp_list2 = ["shruti","preethi"]

emp_list3 = emp_list1 + emp_list2  
print("\nthis is list_addition example\n",emp_list3)

#nested list example

nested_emp_list = [emp_list1,emp_list2,emp_list3]
print("\nnested list example\n",nested_emp_list)
print("\nthe list at postion 2 is: \n",nested_emp_list[2])

#list operations

print("\nlength of nested list is:\n",len(nested_emp_list))        
print("\nmax of nested list is",max(nested_emp_list))        
print("\nmin of nested list is:\n",min(nested_emp_list))       

#additional_list operations

emp_list4 = ["aakash","puneeth","yash","veena","suma","reena"]
print(emp_list4.count(4))
print(emp_list4.index("yash"))
emp_list4.reverse()
print("\n",emp_list4,"\n")
emp_list5 = emp_list4.extend(emp_list3)
print(emp_list5)

print("\n\n======================================================\n\n")

# Employee tuple
emp_tuple1 = ("sumit", "arjun", "nishanth", "keerthikumar")

# Tuple operations

print("\nThe tuple of employees is:\n", emp_tuple1) 

emp_tuple1 = emp_tuple1 + ("amar",)  
print("\nThe append operation\n", emp_tuple1)

emp_tuple1 = emp_tuple1[:2] + ("akbar",) + emp_tuple1[2:]  
print("\nThe insert operation at 2nd position\n", emp_tuple1)

emp_tuple2 = ("shruti", "preethi")

# Tuple addition (concatenation)
emp_tuple3 = emp_tuple1 + emp_tuple2
print("\nThis is tuple_addition example\n", emp_tuple3)

# Nested tuple example
nested_emp_tuple = (emp_tuple1, emp_tuple2, emp_tuple3)
print("\nNested tuple example\n", nested_emp_tuple)
print("\nThe tuple at position 2 is:\n", nested_emp_tuple[2])

# Tuple operations
print("\nLength of nested tuple is:\n", len(nested_emp_tuple))  
print("\nMax of nested tuple is:\n", max(nested_emp_tuple)) 
print("\nMin of nested tuple is:\n", min(nested_emp_tuple))  

# Additional tuple operations
emp_tuple4 = ("aakash", "puneeth", "yash", "veena", "suma", "reena")
print(emp_tuple4.index("yash"))  

print("\n\n======================================================\n\n")

# Employee set
emp_set1 = {"sumit", "shree", "nishanth", "keerthikumar"}

# Set operations

print("\nThe set of employees is:\n", emp_set1)  

emp_set1.add("amar") 
print("\nThe add operation\n", emp_set1)

emp_set2 = {"shruti", "preethi"}

# Set union
emp_set3 = emp_set1.union(emp_set2)
print("\nThis is set_union example\n", emp_set3)

# Set operations
print("\nLength of set is:\n", len(emp_set3))  

# Additional set operations
emp_set4 = {"aakash", "puneeth", "yash", "veena", "suma", "reena"}

#union operation
emp_set5 = emp_set4.union(emp_set3)
print("\nthis is union opertion\n",emp_set5)

#intersection operation

emp_intersection = emp_set5.intersection(emp_list4)
print("\nthis is intersection operation\n",emp_intersection)

emp_diff = emp_set5.difference(emp_set4)
print("\nthis is difference operation\n",emp_diff)

print("\n\n=======================")

employee_info = {'name':'santosh','age':21,'branch':'cse'}
print("The employee info is:\n",employee_info)
print("\nthe type of input is:\n",type(employee_info))

employee_info['salary']=20000
print("\nThe new employee info is:\n",employee_info)

employee_info['projects']=['AI','ML','DSA']
print("\nThe emoloyee projected added are:\n",employee_info)

#accessing the info

employee_info['projects']    
employee_info.get('branch')

#value updating:

employee_info['age'] = 22
print('Updated info')
print(employee_info)

print("\nthe items in the employee are: \n",employee_info.items())
print("\nthe keys in the employee are: \n",employee_info.keys())
print("\nthe values in the employee are: \n",employee_info.values())


