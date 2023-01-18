# How to create a class in pyhton

class Employee:
    # Constructor of the class
    def __init__(self, name, salary):
        #instance variables or instance attributes
        self.emp_name = name
        self.emp_salary = salary
    
    #methods of a class
    def displayEmployeeInfo(self):
        print("Employee name is ", self.emp_name, end = " and ")
        print("Employee salary is ", self.emp_salary)


emp1 = Employee("Gourav", 89000)
emp1.displayEmployeeInfo()