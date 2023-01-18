1. 
Object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

Main Concepts of Object-Oriented Programming (OOPs): 
    Class
    Objects
    Polymorphism
    Encapsulation
    Inheritance
    Data Abstraction

2. In Python, inheritance happens when an object is qualified, and involves searching an attribute definition tree (one or more namespaces). Every time We use an expression of the form object.attr where object is an instance or class object, Python searches the namespace tree at and above object, for the first attr it can find. Because lower definitions in the tree override higher ones, inheritance forms the basis of specialization.

3. 

4. self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.

The reason We need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

Self is always pointing to Current Object.

```
#it is clearly seen that self and obj is referring to the same object
  
class check:
    def __init__(self):
        print("Address of self = ",id(self))
  
obj = check()
print("Address of class object = ",id(obj))
  
# this code is Contributed by Samyak Jain

```

5. Constructors are used to initializing the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization We want to do with your object.

```
# A Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()

```

6. 7. To create a class, use the keyword class:
```
class MyClass:
  x = 5

```
Now we can use the class named MyClass to create objects:
```
p1 = MyClass()
print(p1.x) 

```
The __init__() function:
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

```

8. 
Here, "Robot" is a Super-Class.
"PhysicianRobot" is a sub-Class.

```
class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)
class PhysicianRobot(Robot):
    pass
x = Robot("Marvin")
y = PhysicianRobot("James")
print(x, type(x))
print(y, type(y))
y.say_hi()

```

9. 
Module: A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. 

Class: Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

10. 
Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

11. 
Class attributes are the variables defined directly in the class that are shared by all objects of the class.
Defined directly inside a class.
Shared across all objects.
Accessed using class name as well as using object with dot notation, e.g. classname.class_attribute or object.class_attribute.
Changing value by using classname.class_attribute = value will be reflected to all the objects.

Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor. 
Defined inside a constructor using the self parameter.
Specific to object. 
Accessed using object dot notation e.g. object.instance_attribute.
Changing value of instance attribute will not be reflected to other objects.

12. Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor. 

```
class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

```

13. 
self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.

The reason We need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

```
#it is clearly seen that self and obj is referring to the same object
  
class check:
    def __init__(self):
        print("Address of self = ",id(self))
  
obj = check()
print("Address of class object = ",id(obj))
  
# this code is Contributed by Samyak Jain

```

14. 
Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. We might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

```
# Python program to show use of
# + operator for different purposes.
 
print(1 + 2)
 
# concatenate two strings
print("Geeks"+"For")
 
# Product two numbers
print(3 * 4)
 
# Repeat the String
print("Geeks"*4)

```

15. 
Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. We might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

16. 

17. Inheritance and Polymorphism are fundamental concepts of object oriented programming. These concepts help us to create code that can be extended and easily maintainable.

18. 
Advantage 1: Separating Error-Handling Code from "Regular" Code

Exceptions provide the means to separate the details of what to do when something out of the ordinary happens from the main logic of a program. In traditional programming, error detection, reporting, and handling often lead to confusing spaghetti code.

Advantage 2: Propagating Errors Up the Call Stack

A second advantage of exceptions is the ability to propagate error reporting up the call stack of methods. Suppose that the readFile method is the fourth method in a series of nested method calls made by the main program: method1 calls method2, which calls method3, which finally calls readFile.

Advantage 3: Grouping and Differentiating Error Types

Because all exceptions thrown within a program are objects, the grouping or categorizing of exceptions is a natural outcome of the class hierarchy. An example of a group of related exception classes in the Java platform are those defined in java.io — IOException and its descendants. IOException is the most general and represents any type of error that can occur when performing I/O. Its descendants represent more specific errors. For example, FileNotFoundException means that a file could not be located on disk.

A method can write specific handlers that can handle a very specific exception. The FileNotFoundException class has no descendants.

19. Demerits of not using Error handling:
Disadvantage #1: Experiencing unnecessary overhead
Whenever an exception is thrown, it creates an object and sends data to the log. It’s not much when it comes to a single occurrence of an exception, but what happens if it fails millions of times? Before we know it, the heap gets clogged, the CPU is wasting precious cycles on meaningless tasks, and we can kiss performance goodbye.

Disadvantage #2: Not understanding how the application really works
The best way to figure out how a toy work is by taking it apart. Same goes for applications. We need to increase our application’s Observability. In control theory, Observability is a measure for how well internal states of a system can be inferred by knowledge of its external outputs.
Exceptions are the external outputs that can give us knowledge regarding the state of the application. They give us an exclusive look backstage, which could be especially handy when debugging someone else’s code or working on legacy code.

Disadvantage #3: Filling your logs with noisy events
When an error happens, everyone’s go-to-solution is usually to look at the log. In it they hope to find the needed information to know why did the error happen and if there’s an exception that could help shed more light on it.

Disadvantage #5: Inability to focus on what actually matters
Exceptions cloud the developer’s view. As exception numbers increase, it’s harder to know which exceptions are more important than others. This could lead to missing a major issue or dismissing an exception that requires immediate attention.

20. 
If We have some suspicious code that may raise an exception, We can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.
We can also provide a generic except clause, which handles any exception. After the except clause(s), We can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception. The else-block is a good place for code that does not need the try: block's protection.

21. 

22. 

23. The try statement works as follows.

    a) First, the try clause (the statement(s) between the try and except keywords) is executed.
    b) If no exception occurs, the except clause is skipped and execution of the try statement is finished.
    c) If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.
    d) If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

24. 
a) Try/Except/Else

When attaching an else statement to the end of a try/except, this code will be executed after the try has been completed, but only if no exceptions occur.

We can take the previous example of prompting a user for an integer input and use an else block to thank them for valid input and breaking out of the while loop.

```
while True:
  try:
    num = int(input("Enter an int: "))
  except Exception as e:
    print(e)
  else:
    print("Thank you for the integer!")
    break# Enter an int: a
# invalid literal for int() with base 10: 'a'
# Enter an int: 3
# Thank you for the integer

```

b) Try/Except/Finally

When attaching a finally statement to the end of a try/except, this code will be executed after the try has been completed, regardless of exceptions.

Again, we’ll use our previous example and add a simple counter to illustrate this behavior.

```
count = 0
while True:
  try:
    num = int(input("Enter an int: "))
    break
  except Exception as e:
    print(e)
  finally:
    count += 1
    print("Attempt #:",count)# Enter an int: a
# invalid literal for int() with base 10: 'a'
# Attempt #: 1
# Enter an int: 3
# Attempt #: 2

```

25. The raise statement is used to raise or throw an exception in Python. It is used to indicate that a specific error or exception has occurred in the program, and it can be used to provide a custom error message. The raise statement can also be used to re-raise an exception that was caught in a try-except block, allowing it to be handled by an outer try-except block or the program's global exception handler.

26. The assert statement is used to test if a given condition is true, and if it is not, it raises an AssertionError exception with an optional error message. The assert statement is used to check for conditions that should never occur in the program and can be used as a quick way to check for errors in the code during development and debugging.

The assert statement is similar to the raise statement in that it can be used to indicate an error in the program, but it is intended to be used for testing and debugging purposes, whereas raise is intended to be used for signaling a specific exception in the program.

27. The with statement in Python is used to wrap the execution of a block of code with methods defined by a context manager. The as argument is used to assign a variable to the context manager, which can then be used to interact with the context that the manager manages. The with statement is used to ensure that certain resources are properly acquired and released, such as file handles, database connections, and locks.

A common use case is working with files, where the with statement is used to open a file and automatically close it after the block of code is executed, regardless of whether an exception was raised or not.

The with statement is similar to the try/finally statement in that it is used to ensure that certain actions are taken, regardless of whether an exception is raised or not. However, the with statement is more concise and easy to read, as it eliminates the need to explicitly write the try/finally block and the boilerplate code that goes with it.

28. In Python, *args and **kwargs are used as a way to pass a variable number of arguments to a function.

*args is used to pass a non-keyworded, variable-length argument list to a function. It allows a function to receive an arbitrary number of arguments, and the arguments are passed as a tuple to the function.

**kwargs is used to pass a keyworded, variable-length argument list to a function. It allows a function to receive an arbitrary number of keyword arguments, and the arguments are passed as a dictionary to the function.

*args and **kwargs can be used together in a function definition, and the order of the parameters should be *args, **kwargs.

For example, a function that takes any number of arguments and print them:

```
def print_args(*args, **kwargs):
    print(args)
    print(kwargs)

print_args(1, 2, 3, a=4, b=5, c=6)

```

This will print:
```
(1, 2, 3)
{'a': 4, 'b': 5, 'c': 6}

```

It's worth noting that you can also use these syntaxes when calling a function, to pass a tuple or dictionary of arguments respectively.

29. In Python, you can pass optional or keyword parameters from one function to another by using the * and ** operators in the function call.

When calling a function, you can use the * operator to pass the elements of a tuple or list as separate positional arguments, and the ** operator to pass the elements of a dictionary as separate keyword arguments.

For example, consider a function foo that takes three parameters, and a function bar that takes a variable number of arguments and keyword arguments,

```
def foo(a, b, c):
    print(a, b, c)

def bar(*args, **kwargs):
    print(args)
    print(kwargs)

# call bar with parameters of foo
bar(*(1,2,3))
bar(**{'a':1,'b':2,'c':3})

```

The first call to bar will pass the tuple (1, 2, 3) as separate positional arguments, and the second call will pass the dictionary {'a': 1, 'b': 2, 'c': 3} as separate keyword arguments.

You can also use the * and ** operators in the function definition to accept a variable number of arguments and keyword arguments, which is known as the *args and **kwargs pattern.

Another way is to use functools.partial, that allows creating a new function with some of the arguments of another function fixed.

```
from functools import partial

def foo(a, b, c):
    print(a, b, c)

# create a new function bar with a fixed first parameter
bar = partial(foo, 1)
bar(2,3)

```
This will call foo with the parameters 1,2,3.

30. In Python, a lambda function is a small, anonymous function that is defined using the lambda keyword. Lambda functions are also known as anonymous functions or throwaway functions, because they are not bound to a name and are typically used only once.

A lambda function is defined using the following syntax:

```
lambda argument_list: expression

```

Where argument_list is a comma-separated list of arguments and expression is a single expression that is evaluated when the function is called.

For example, the following lambda function takes two arguments and returns their sum:

```
sum = lambda x, y: x + y
print(sum(1, 2)) # 3

```

Lambda functions are often used as arguments to higher-order functions, such as map(), filter() and reduce(), which take one or more functions as arguments and return a new function. They can also be used as arguments to other functions, like sorted() to provide a custom sorting key.

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8, 10]

```

Lambda functions are restricted in their functionality, they can only contain expressions and cannot contain statements or multiple expressions. They are also limited to a single expression and do not have a return statement.

31. Inheritance is a mechanism in object-oriented programming (OOP) languages like Python that allows one class to inherit properties and methods from another class.

In Python, a class can inherit from one or multiple classes, and the class that inherits from another class is called a subclass or derived class, while the class from which it inherits is called the superclass or base class.

A subclass can inherit properties and methods from a superclass, and it can also override or add new properties and methods. This allows for code reuse and a more organized and efficient codebase.

For example, let's say we have a class Animal that contains properties and methods that are common to all animals, such as name and speak().

```
class Animals:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

```

We could then create a subclass Dog that inherits from the Animals class, and add new properties and methods specific to dogs, such as breed.

```
class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        return 'bark'

```

In this example, the Dog class inherits the name property and the speak() method from the Animals class, and it also has a new property breed and it has overridden the method speak() to return 'bark'.

This way, we can create an object of class dog and it will have all the properties of class Animals and it's own properties as well.

```
dog1 = Dog('dog1','Golden Retriever')
print(dog1.name) # 'dog1'
print(dog1.breed) # 'Golden Retriever'
print(dog1.speak()) # 'bark'

```

Inheritance can also be multiple, where a class can inherit from more than one class, also known as multiple inheritance. This can lead to complex class hierarchies and naming conflicts, so it's important to use it with care.

32. In Python, when a class C inherits from multiple classes A and B using the syntax class C(A,B), and both classes A and B have their own version of the method func(), the order of the base classes in the class definition matters. The method from the first base class listed in the class definition is given priority, and it will be the version of the method that gets invoked when called from an object of class C.

For example, if the class definition is class C(A, B) and both classes A and B have their own version of func(), then the version of func() from class A will be invoked when called from an object of class C.

```
class A:
    def func(self):
        print("from A")

class B:
    def func(self):
        print("from B")

class C(A, B):
    pass

c = C()
c.func() # prints "from A"

```

If the class definition is class C(B, A), then version of func() from class B will be invoked when called from an object of class C.

```
class A:
    def func(self):
        print("from A")

class B:
    def func(self):
        print("from B")

class C(B, A):
    pass

c = C()
c.func() # prints "from B"

```

It's worth noting that python uses C3 algorithm to resolve method resolution order(MRO) when it comes to multiple inheritance, that starts by looking in the current class, then looks in the direct base classes and then in their base classes and so on. If the method is not found in any of them, it will look for method resolution order defined by the programmer in the class definition.

33. In Python, there are several built-in functions and methods that can be used to determine the type of an instance and its inheritance:

    a) `type(object)`: This built-in function returns the type of the object passed as an argument. It can be used to determine the type of an instance, for example type(5) returns <class 'int'>, type("hello") returns <class 'str'>.

    b) `isinstance(object, classinfo)`: This built-in function returns True if the object is an instance of the classinfo or a subclass thereof, and False otherwise. It can be used to check if an object is an instance of a specific class or one of its subclasses, for example isinstance(5, int) returns True, isinstance("hello", str) returns True.

    c) `issubclass(class, classinfo)`: This built-in function returns True if the class is a subclass (direct or indirect) of classinfo, and False otherwise. It can be used to check if a class is a subclass of another class, for example issubclass(Dog, Animals) returns True if Dog is a subclass of Animals.

    d) `object.__class__`: This attribute returns the class to which an object belongs.

    e) `object.__base__`: This attribute returns the base class of an object.

    f) `object.__mro__`: This attribute returns the method resolution order of an object, which is a tuple of classes that are searched, in order, by Python to determine the first object with a particular attribute.

    g) `super()`: This built-in function returns a temporary object of the superclass, which allows you to call its methods.

All of the above methods are used to check the type of an instance and its inheritance, with isinstance() and issubclass() being the most commonly used ones.

34. The `nonlocal` keyword in Python is used to indicate that a variable is non-local to the current function. This means that the variable is defined in an enclosing scope, typically in a parent or enclosing function. When a non-local variable is assigned a new value, the assignment affects the variable in the enclosing scope, rather than creating a new local variable with the same name. The `nonlocal` keyword is only valid in the body of a nested function, and it is only necessary when the variable being assigned to has the same name as a variable defined in an enclosing scope.

35. The `global` keyword in Python is used to indicate that a variable is a global variable, which means that it is accessible from anywhere in the code, including both the current function and any other functions or code outside of the current function. When a global variable is assigned a new value, the assignment affects the variable in the global scope, rather than creating a new local variable with the same name.

The `global` keyword is used inside a function to indicate that a variable is a global variable, and not a local variable. When a variable is defined with global keyword, it can be accessed and modified from anywhere in the code, including inside the functions. It is important to note that, if a variable is defined as global, it will not be defined as a local variable inside a function even if that function defines a variable with the same name.