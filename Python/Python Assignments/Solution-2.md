1. Python is a high-level general-purpose programming language that can be applied to many
different classes of problems.
    The language comes with a large standard library that covers areas such as string
processing (regular expressions, Unicode, calculating differences between files), internet
protocols (HTTP, FTP, SMTP, XML-RPC, POP, IMAP), software engineering (unit testing, logging,
profiling, parsing Python code), and operating system interfaces (system calls, filesystems,
TCP/IP sockets).

2. Python is called dynamically typed language because it doesn’t know about the type of the
variable until the code is run. So declaration is of no use. What it does is, It stores that
value at some memory location and then binds that variable name to that memory container
Moreover, it makes the contents of the container accessible through that variable name. So the
data type does not matter. As it will get to know the type of the value at run-time.

3. Pros
Beginner-friendly
Large Community
Flexible and Extensible
Extensive Libraries
Embeddable
Highly Scalable
IoT Opportunities
Portable

Cons
Issues with design
Slower than compiled languages
Security
Work Environment
High memory consumption
Dynamically-typed language
Complex multithreading
Garbage collection leads to potential memory losses

4. Top 5 domains where we can use Python
Web Development, Data Science, OS devlopment, Scientific Programming, Gaming

5. Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

Syntax: 

```
x = 5
y = "John"
print(x)
print(y)

```

6. We can take input in pyhton using the input() function.

7. By default, input returns a string. So the name and age will be stored as strings

8. Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

9. Yes. We can use functions like split(), map(), List Comprehension

Using split():

```
$a, b = input("Enter two of your lucky number: ").split() 
$print("First lucky number is: ", a) 
$print("Second lucky number is: ", b) 

```


Output:
Enter two of your lucky number: 7 1
First lucky number is: 7
Second lucky number is: 1

using map():

```
$x, y = map(int, input("Enter two values: ").split())
$print("First Number is: ", x) 
$print("Second Number is: ", y)

```


Output:
Enter two values: 7 1
First Number is: 7
Second Number is: 1

using List Comprehension

```
$x, y = [x for x in input("Enter your name and age: ").split(",")]
$print("Your name is: ", x) 
$print("Your age is: ", y)

```


Output:
Enter your name and age: FACE Prep, 8
Your name is: FACE Prep
Your age is: 8

10. Keyword is a closely related or associated word that is reserved by a program because, the word has a special meaning that defines commands and specific parameters for that code set.

11. We cannot use keywords as variable names. It's because keywords have predefined meanings.

12 Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

13. To throw (or raise) an exception, use the raise keyword.

14. Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

15. In Python programming, you can perform division in two ways. The first one is Float Division("/") and the second is Integer Division("//") or Floor Division.

16. Code: 

```
$str = "iNeuron"
$print(str*4)

```

17. 
```
$num = int(input("Please Enter the number to be checked."))
$if num % 2 == 0:
$   print("The number is even.")
$else:
$   print("The number is odd.")

```

18. Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused and productive results.

19. What will the output of the following?
```
1 or 0 = TRUE

0 and 0 = FALSE

True and False and True = FALSE

1 or 0 or 0 = TRUE

20. Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

21. The if/elif/else structure is a common way to control the flow of a program, allowing you to execute specific blocks of code depending on the value of some data.

--> if statement: If the condition following the keyword if evaluates as true, the block of code will execute. Note that parentheses are not used before and after the condition check as in other languages.

```
$if True:
$  print('If block will execute!')

```

```
$x = 5

$if x > 4:
$  print("The condition was true!") #this statement executes

```

--> else statement:You can optionally add an else response that will execute if the condition is false:

```
$if not True:
$  print('If statement will execute!')
$else:
$  print('Else statement will execute!')

```

Or you can also see this example:

```
$y = 3

$if y > 4:
$  print("I won't print!") #this statement does not execute
$else:
$  print("The condition wasn't true!") #this statement executes

```

Note that there is no condition following the else keyword - it catches all situations where the condition was false


--> elif statement: Multiple conditions can be checked by including one or more elif checks after your initial if statement. Just keep in mind that only one condition will execute:

```
$z = 7

$if z > 8:
$  print("I won't print!") #this statement does not execute
$elif z > 5:
$  print("I will!") #this statement will execute
$elif z > 6:
$  print("I also won't print!") #this statement does not execute
$else:
$  print("Neither will I!") #this statement does not execute

```

Note: only the first condition that evaluates as true will execute. Even though z > 6 is true, the if/elif/else block terminates after the first true condition. This means that an else will only execute if none of the conditions were true.

22. 
```
$age_of_a_person = int(input("Please enter your age."))
$if age_of_a_person >= 18:
$    print("I can vote")
$else:
$    print("I can't vote")

```

23. 
```
$numbers = [12, 75, 150, 180, 145, 525, 50]
$
$sum_of_evens  = 0
$for num in numbers:
$    if(num%2 == 0):
$        sum_of_evens += num
$
$print("The sum of evens in the given list is:", sum_of_evens)

```

24.
```
$a, b, c = input("Enter three numbers.").split()
$print("The maximum of three numbers are:", max(a,b,c))

```

25.
```
$numbers = [12, 75, 150, 180, 145, 525, 50]
$ans = list()
$for num in numbers:
$    if(num % 5 == 0):
$        if(num > 150 and num < 500):
$            continue
$        if(num > 500):
$            break
$        ans.append(num)
$
$print(ans)\

```

26. In Python, Strings are arrays of bytes representing Unicode characters. Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

Strings in Python can be created using single quotes or double quotes or even triple quotes. 

Syntax:
$string s1 = "This is a string."

27. You can access the characters in a string by referring to its index number inside square brackets [] .

28. 
```
string = "Big Data iNeuron"
print(string[8:])

```

29. 
```
string = "Big Data iNeuron"
print(string[-1:-8:-1])

```

30. 

```
string = "Big Data iNeuron"
reversed_string = string[-1:0:-1]

```

31. An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.

32. 
An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.

33. 
```
print("iNeuron's Big Data Course")
```

34.
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data. List items are ordered, changeable, and allow duplicate values.

35. To create a list in Python, we use square brackets ([]). Here's what a list looks like:

Method 1:
ListName = [ListItem, ListItem1, ListItem2, ListItem3, ...]

Method 2:
ListName = list()

36. Using the [] brackets we can access the elements of a list.

37. 
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

```

38. 
```
input_list = list()

while(True):
    str = input("Enter the number you wabt to append in list. Enter \"I dont want to enter anymore\" to break the loop.")
    if (str == "I dont want to enter anymore"):
        break
    input_list.append(int(str))

print(input_list)
print("The length of the list is", len(input_list))

```

39. 
```
lst = ["Welcome", "to", "Data", "course"]
lst.insert(3,"Big")

print(lst)

```

40. Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

41. tup1 = tuple()

42. We can't add elements to a tuple because of their immutable property.

43. We can use '+' operator to append two tuples.
```
# input tuple 1
inputTuple_1 = (12, 8, 6)
# input tuple 2
inputTuple_2 = (3, 4)
# appending/concatenating 2nd tuple to the first tuple using the + operator
resultTuple = inputTuple_1 + inputTuple_2
# printing the resultant tuple after appending
print("Resultant tuple after appending inputTuple_2 to the inputTuple_1:", resultTuple)

```

44. 

```
input_tuple = (1,2,3,4,5,6,7,8,9)

print(input_tuple)
print("The length of the list is", len(input_tuple))

```

45. Sets:
    1. Sets are used to store multiple items in a single variable.
    2. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
    3. A set is a collection which is unordered, unchangeable*, and unindexed.

46. Creating a set in Python:
```
input_set = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9}

print(input_set)

```
We can declare sets using {} braces and also by using explicit type-casting.

47. 
```
input_set = {'abc', 'def', 'abc', 'Hello', 'No!'}

input_set.add('iNeuron');
print(input_set)

```

48. update() is used to add multiple values in python set.
```
input_set = {'abc', 'def', 'abc', 'Hello', 'No!'}

input_set.update(['iNeuron', 'Help'])
print(input_set)

```

49. To add one item to a set use the add() method.
To add more than one item to a set use the update() method.

50. It clears the entries of the set.

51. The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
Syntax:
    frozenset(iterable)
example:
```
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
# x.update(["strawberry"])
print(x)

```

52. In frozenset() we cannot update the set. But in set() we can add new entries, i.e; we can update the set.

53. The union() method returns a set that contains all items from the original set, and all items from the specified set(s). You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item.
Syntax:
    set.union(set1, set2...)

Example:
```
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result) 

```

54. The intersection() method returns a set that contains the similarity between two or more sets.
Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
Syntax:
    set.intersection(set1, set2 ... etc)

Example:
```
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result) 

```
55. Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

56. 

57. 
```
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

```

58. 
Output:
```
<class 'dict'>

```
59. 
```
dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is: ", dict)

# using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value

dict['key3'] = 'geeks'
print("Updated Dict is:", dict)

```

60. 

```
dict = {}
dict['name'] = "abc"
dict['age'] = 13
dict['skills'] = ["C/C++", "Python", "ReactJS", "Material UI", "Redux", "Golang"]
dict['states_visited'] = ["Goa", "TN", "UP","Bihar","Jharkhand","Kerala","Karnataka","Haryana","Delhi"]

for key, value in dict.items():
    print("Key = ", key, "and corresponding Value is: ", value)

```

61. 
```
dict = {}
dict['name'] = "abc"
dict['age'] = 13
dict['dict2'] = {"Front-end tech stacks": ["JavaScript", "TypeScript"], "Back-end tech stacks": ["Golang", "Java"]}
dict['states_visited'] = ["Goa", "TN", "UP","Bihar","Jharkhand","Kerala","Karnataka","Haryana","Delhi"]

for key, value in dict.items():
    if key == 'dict2':
        nested_dict = dict[key]

for key, value in nested_dict.items():
    print("Nested Key is", key, "and the Corresponding value is", value)


```

62. The get() method returns the value of the item with the specified key.
Syntax
    dictionary.get(keyname, value)
Example:
```
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)

```


63. The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

The view object will reflect any changes done to the dictionary, see example below.
Syntax:
    dictionary.items()
Example:
```
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x) 

# Note: When an item in the dictionary changes value, the view object also gets updated.

```


64. The pop() method removes the element at the specified position.
Syntax:
    list.pop(pos)
Example:
```
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1) 

# Note: pop() returns the removed element.

```

65. The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.
Syntax:
    dictionary.popitem()

Example:
```
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x) 

# Note: Returns the last item inserted in the dict. In this case it is "('year', 1964)".

```

66. The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
Syntax:
    dictionary.keys()

Example:

```
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x) 

# Note: When an item is added in the dictionary, the view object also gets updated.

```

67. The values() method returns a view object. The view object contains the values of the dictionary, as a list
Syntax:
    dictionary.values()

Example:
```
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x) 

# Note: When a values is changed in the dictionary, the view object also gets updated.

```

68. Looping means repeating something over and over until a particular condition is satisfied. A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied. Such a type of statement is also known as an iterative statement.

69. There are two types of loops in python.
    1. In python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.
        Syntax :
            while expression:
                statement(s)

        Example:
        ```
            # Python program to illustrate
            # while loop
            count = 0
            while (count < 3):   
                count = count + 1
                print("Hello Geek")
        ```
 
    2. For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is “for in” loop which is similar to for each loop in other languages. Let us learn how to use for in loop for sequential traversals.

        Syntax:
            for iterator_var in sequence:
                statements(s)

    It can be used to iterate over a range and iterators.

        Example:
        ```
            # Python program to illustrate
            # Iterating over range 0 to n-1
             
            n = 4
            for i in range(0, n):
                print(i)
        ```


70. 
The for loop is used when we already know the number of iterations, which means when we know how many times a statement has to be executed. That is why we have to specify the ending point in the for loop initialization. When we need to end the loop on a condition other than the number of times, we use a while loop.

71. Python Continue statement is a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code inside the loop for the current iteration only, i.e. when the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped for the current iteration and the next iteration of the loop will begin.

Syntax:
    while True:
        ...
        if x == 10:
            continue
        print(x)

Example:
    ```
    for var in "Geeksforgeeks":
        if var == "e":
            continue
        print(var)
    ```

72. Python break is used to terminate the execution of the loop. 
Syntax:
    Loop{
        Condition:
            break
        }
Example:
    ```
    for i in range(10):
        print(i)
        if i == 2:
            break
    ```

73. The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

74. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax:
range(start, stop, step)

Example 1:
```
x = range(3, 6)
for n in x:
  print(n)
```

Example 2:
```
x = range(3, 20, 2)
for n in x:
  print(n) 
```

75. 
Looping through the keys:
```
for x in thisdict:
  print(x)
```

Looping through the values:
```
for x in thisdict:
  print(x)
```

Looping through the key value pairs:
```
for key, value in thisdict.items():
  print(key, value) 
```

### Coding problems
76. 
```
def factorial(num):
    res = 1;
    for i in range (1, num+1):
        res = res * i
    return res;

num = int(input("Please enter the number."))
print(factorial(num))
```

77. 
```
def simple_interest(P, R, T):
    return P*R*T/100

P = float(input("Please enter the principal."))
R = float(input("Enter the rate of interest."))
T = float(input("Enter the time you want to invest you money for."))

print("The simple interest on your principal is:", simple_interest(P, R, T))
```

78. 
```
def compound_interest(P, R, T):
    return P*((1+(R/100))**T) - P

P = float(input("Please enter the principal."))
R = float(input("Enter the rate of interest."))
T = float(input("Enter the time you want to invest you money for."))

print("The compound interest on your principal is:", compound_interest(P, R, T))
```

79. 
```
# Check Prime
import math
def isPrime(n):
    if (n == 0 or n == 1):
        print("The number is niether prime nor composite.")
        return
    flag = True
    for i in range (2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            flag = False
            break
    
    if(flag):
        print("The number is Prime.")
    else:
        print("The number is Composite.")

```

80. 
```
def isArmstrong(n):
    num = n
    sum = 0
    while(n):
        rem = n % 10
        sum += rem**3
        n = n // 10
    if (sum == num):
        print("The number is Armstrong.")
    else:
        print("The number is not Armstrong.")

```

81. 
```
def Fibbonacci(n):
    if ( n == 1 or n == 2):
        return 1
    a = 1
    b = 1
    c = 0

    for i in range(3, n+1):
        c = a + b;
        a = b;
        b = c;
    
    return c;

```

82. 
```
list_of_nums = [1,2,3,4,5,6,7,8,9]
# Using Swapping technique
num = list_of_nums[0]
list_of_nums[0] = list_of_nums[-1]
list_of_nums[-1] = num

print(list_of_nums)

```

83. 
```
list_of_nums = [1,2,3,4,5,6,7,8,9]
# Let the two indices be 2 and 5
num = list_of_nums[2]
list_of_nums[2] = list_of_nums[5]
list_of_nums[5] = num

print(list_of_nums)

```

84. 
```
list_of_nums = [6,1,2,3,4,5,7,8,9]
list_of_nums.sort()
# Lets say we want 5th largest element.
print(list_of_nums[5-1])

```

85. 
```
list_of_nums = [6,1,2,3,4,5,7,8,9]
list_of_cumulative_sums = list()
list_of_cumulative_sums.append(list_of_nums[0])
for i in range (1, len(list_of_nums)):
    list_of_cumulative_sums.append(list_of_cumulative_sums[i-1] + list_of_nums[i])
print(list_of_cumulative_sums)

```

86. 
```
str = "TATA"
str_rev = str[::-1]

if(str == str_rev):
    print("The string is pallindrome.")
else:
    print("The string is not pallindrome.")

```

87. 
```


```

88. 
```

```

89. 
```

```

90. 
```
# Since set() contains unique values we use set as data structure to recieve our goal.

given_dict = {"name": "abc", "age": 26, "address": "WB"}
set_of_unique_values = set()

for v in given_dict.values():
    set_of_unique_values.add(v)

print(set_of_unique_values)
```

91. 
```
def Merge(dict1, dict2):
    res = {**dict1, **dict2}

    return res

dict1 = {"name": "abc", "age": 26, "address": "WB"}
dict2 = {"job": "SDE", "city": "KOAA"}

print(Merge(dict1, dict2))

```

92. 
```
# List of tuples to dictionary
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

given_list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
res = {}
for ele in given_list:
    dict1 = {}
    dict1[ele[0]] = ele[1]
    res = Merge(res, dict1)

print(res)

```

93. 
```
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

given_list = [9, 5, 6]
res = []
for ele in given_list:
    tuple1 = (ele, ele**3)
    res.append(tuple1)

print(res)

```

94. 
```
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)
res = []

for ele1 in test_tuple1:
    for ele2 in test_tuple2:
        tuple1 = (ele1, ele2)
        res.append(tuple1)

for ele1 in test_tuple2:
    for ele2 in test_tuple1:
        tuple1 = (ele1, ele2)
        res.append(tuple1)

print(res)

```

95. 
```
def sort_Tuple(tup):
    tup.sort (key = lambda x : x[1])
    return tup

tup = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
print(sort_Tuple(tup))

```

96. 
```
def print_stars(n):
    for i in range (1, n+1):
        for j in range (1, i + 1):
            print("*", end=" ")
        print("\n")

print_stars(5)

```
97. 
```
def print_stars(n):
    for i in range (1, n+1):
        for j in range (n, i, -1):
            print(" ", end=" ")
        for k in range (1, i+1):
            print("*", end=" ")
        print("\n")

print_stars(5)

```

98. 
```
def print_stars(n):
    for i in range (1, n+1):
        for j in range (n, i, -1):
            print(" ", end=" ")
        for k in range (1, i+1):
            print("*", end="   ")
        print("\n")

print_stars(5)

```

99. 
```
def print_nums(n):
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(j, end=" ")
        print("\n")

print_nums(5)

```

100. 
```
def print_nums(n):
    num = 65
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(chr(num), end=" ")
        print("\n")
        num = num + 1

print_nums(5)

```