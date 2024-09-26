class Employee:
     
     def __init__(self,Id,Name,Salary) :
        self.id=Id
        self.name=Name
        self.__salary = Salary

     def printDetails(self):
       print(f"Employee ID:{self.id}")  
       print(f"Employee Name:{self.name}")      
       print(f"Employee Salary:{self.salary}") 

     @property
     def getEmpSalary(self):
      
      
       return self.__salary   


emp = Employee(101,"Rakesh",10000)

print(emp.getEmpSalary)