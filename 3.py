# Employee details program
class Employee:
	def __init__(self, name, salary, age):
		self.Employee_name=name
		self.Employee_salary=salary
		self.Employee_age=age
	def getName(self):
		return(self.Employee_name)
	def getsalary(self):
		return(self.Employee_salary)
	def getage(self):
		return(self.Employee_salary)

emp1= Employee("Ram",100,12)
emp2= Employee("Sita",200,19)
print ("Employee Name= ",emp1.getName())
print ("Employee Salary= ",emp1.getsalry())
print ("Employee age= ",emp1.getage())
print ("Employee Name= ",emp2.getName())
print ("Employee Salary= ",emp2.getsalry())
print ("Employee age= ",emp2.getage())


