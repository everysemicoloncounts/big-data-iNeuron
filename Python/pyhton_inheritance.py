# Inheritance in python

#Base Class aka Parent Class
class Person():

    def __init__(self, name):
        self.person_name = name

    def display_person_details(self):
        print("The name of the person is", self.person_name)

    def isEmployed(self):
        print(self.person_name, "is un-employed")


#Derived class aka Child Class
class Employee(Person):

    def __init__(self, name, id_num, salary, designation):
        self.emp_id = id_num
        self.emp_salary = salary
        self.emp_designation = designation

        # #Calling constuctor of the base class (Method 1)
        # Person.__init__(self, name)

        #Method 2: Using super keyword
        super().__init__(name)


    def display_emp_details(self):
        print("The name of the emp is", self.person_name,".")
        print("The employee id of the employee is", self.emp_id,".")
        print("The person is getting", self.emp_salary, "as salary.")
        print("The person is working as", self.emp_designation,".")

    def isEmployed(self):
        print(self.person_name, "is Employed.")

emp1 = Person("abc")
emp1.display_person_details()
emp1.isEmployed()

print()

emp2 = Employee("Rahul", 171, 89000, "Associate")
emp2.display_emp_details()
emp2.isEmployed()
emp2.display_person_details()
print(emp2.person_name)


