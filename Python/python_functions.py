## Functions in python

# Examples of in-built functions
list = [1,2,3,4,5,6,7,8,9,10,11,12]
print("The maximum in the list is: ", max(list))
print("The minimum in the list is: ", min(list))
print("The sum of all the elements in the list is: ", sum(list))

# Defining a function

def welcome_message(name):
    print("Welcome", name)

welcome_message("Pompia")

def bot_message():
    return "This is a bot message"


## WAF to calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result = result * i
        return result

print(factorial(5))

## Return Multiple values from a function

a,b,c = 1,2,3
print(a,b,c)

def square_and_cube(num):
    return num**2, num**3

print(square_and_cube(5))

## Non key-value arguments
def example_nonkeyed_args(*argv):
    for params in argv:
        print(params)

example_nonkeyed_args("Hello", 5, [2,4], {1,7}, {"name": 'abc', "add": 'blr'})

## key-value arguments in python

def example_of_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, ":",v)

example_of_kwargs(host='170.80.80.80', port=9841, password='abcd')