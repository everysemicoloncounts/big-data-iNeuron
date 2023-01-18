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

emp1.emp_count = 5
emp2.emp_count = 7
print(emp1.emp_count)
print(emp2.emp_count)
print(Employee.emp_count)

# What is static method in python??

class Car:

    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color

    def displayCarDetails(self):
        print("The name of the car is", self.car_name, end = ". ")
        print("The car is of",self.car_color,"color.")

    @staticmethod
    def welcome_message():
        print("This is a nice color")

Car.welcome_message()

car1 = Car("XUV 700", "black")
car2 = Car("Supra", "white")

car1.displayCarDetails()
car2.displayCarDetails()

car1.welcome_message()
car2.welcome_message()