#Assignment:inheritance

#simple employee class:

class emp_details():
    def emp1(self):  
        print("Employee 1: Nishanth")

    def emp2(self):
        print("employee 2 : Sumit")

    def emp3(self):
        print("employee 3: Shreeram")

emp = emp_details()
emp.emp1()
emp.emp2()
emp.emp3()

print("\n========\n")
#employee info with constructor

class emp_with_constructor():
    def __init__(self,name,sector,salary,exp,city):
        self.name = name
        self.sector = sector
        self.salary = salary
        self.exp = exp
        self.city = city

empd = emp_with_constructor("Nishanth","Full stack web development",700000,"5 years","Mysuru")
print(empd.name)
print(empd.sector)
print(empd.salary)
print(empd.exp)
print(empd.city)

print("\n===========\n")


#default passing and initializing the values (usage of the constructors)

class emp_with_default_values():
    def __init__(self,name="Nishanth",sector="FSD",salary="850000",exp="4.5 years"):
        self.name = name
        self.sector = sector
        self.salary = salary
        self.exp = exp

    def person_info(self):
        return ({self.name},{self.sector},{self.salary},{self.exp})

empdv = emp_with_default_values()
print(empdv.name)
print(empdv.sector)
print(empdv.salary)
print(empdv.exp)


print("\n=====================\n")
#INHEITERITANCE
#single inheritence


class employee_inheritance:
    def __init__(self,name,post):
        self.name = name
        self.post = post

    def about(self):
        print("Employee name is " + self.name)
        print("employee post is "+ str(self.post))

class non_working_staff(employee_inheritance): #inheritence
    def stateprofession(delf):
        print("I am a peon")

emp_inherit = employee_inheritance("Ram","peon")
print("My name is : \n",emp_inherit.name)
print("The post i work for: \n",emp_inherit.post)

print("\n=====================\n")

#multiple inheritence

class employee_role:
    def main_work(self):
        print("I am a full stack developer")

class alter_work:
    def alter_job(self):
     print("I am a part-time programmer")

class employee_multiple_inheritence(employee_role,alter_work):
    pass

emi = employee_multiple_inheritence()
print("Hi, I am Nishanth")
emi.main_work()
emi.alter_job()

print("\n=====================\n")

#multilevel inheritance
class Employee:
    def work(self):
        print("Employee can work")

class Manager(Employee):
    def manage(self):
        print("Manager can manage")

class Engineer(Manager):
    def develop(self):
        print("Engineer can develop")

#objects

e = Engineer()
e.work()
e.manage()
e.develop()


print("\n=====================\n")

#hirarchical inheritence

class office:
    def profession(self):
        print("I work for Infosys")

class shreeram(office):
    def web_dev(self):
        print("I am a full stack dev")

class keerthi(office):
    def da(self):
            print("I am a data analyst")

dev = shreeram()
dev.profession()
dev.web_dev()

data_an = keerthi()
data_an.profession()
data_an.da()
