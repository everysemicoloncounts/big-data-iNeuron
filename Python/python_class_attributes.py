## Diff bet. class varaible and instance variable
# https://www.geeksforgeeks.org/difference-between-instance-variable-and-class-variable/

# A varaible that is shared among all the class' objects such as the variables defined using "static" keyword

class Employee:

    #Class attribute
    emp_count = 0

    # Constructor of the class
    def __init__(self, name, salary):
        #instance variables or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.emp_count += 1
    
    #methods of a class
    def displayEmployeeInfo(self):
        print("Employee name is ", self.emp_name, end = " and ")
        print("Employee salary is ", self.emp_salary)

    def displayEmployeeCount(self):
        print("Total numbers of employees are:", Employee.emp_count)

emp1 = Employee("abc", 1000)
emp1.displayEmployeeCount()
emp2 = Employee("bcd", 150)
emp1.displayEmployeeCount()