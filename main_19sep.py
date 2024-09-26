# static methods and class methods
'''
class Employee:
    comName = "MicroSoft"

    def __init__(self,id,Salary):
        self.id = id
        self.Salary = Salary

print(Employee.comName)
Employee.comName = "Tesla"
print(Employee.comName) 

rakesh=Employee(102,45000)
print(rakesh.comName)

raju=Employee(105,30000)
raju.co="cocacola"
print(raju.co)
'''

# class methods and class Attribute

class Employee:
    ComName="Microsoft"

    def __init__(self,id,Salary):
        self.id=id
        self.Salary=Salary

    @classmethod
    def changeCompany(cls,newCompany)  :
        cls.ComName=newCompany

Employee.changeCompany("Google")

rakesh=Employee(102,45000)
print(rakesh.ComName)

raju=Employee(105,30000)
print(raju.ComName)



