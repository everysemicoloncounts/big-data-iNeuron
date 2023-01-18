# Creating Lambda functions

lambda_add_two_nums = lambda num1,num2: num1 + num2
print(lambda_add_two_nums(7,5))

## Write a lambda expression to concatinate two strings

lambda_concatinate_two_strings =  lambda str1, str2: str1 + str2
print(lambda_concatinate_two_strings("Hello"," World"))

## lambda to find the max of two nums

lambda_max_of_two_nums = lambda num1, num2: num1 if num1 >= num2 else num2
print(lambda_max_of_two_nums(4,2))


## Map function in python
list1 = [1,2,3,4,5,6,7,8,9,10]

lambda_square = lambda num: num**2
square_list = map(lambda_square, list1)
print(list(square_list))

#add sequential respective elememnts from two elements
list1 = [1,2,3,4,5,6]
list2 = [2,4,6,8,10,12]

lambda_add_two_nums = lambda num1, num2: num1 + num2

add_two_list = map(lambda_add_two_nums, list1, list2)
print(list(add_two_list))



## Reduce function in python
# at the end we will get one final value and not an iterable.
# reduces the iterable to a single value

# How to reduce ??
import functools
list_x = [1,2,3,4]

sum_of_a_list = functools.reduce(lambda_add_two_nums, list_x)
print(sum_of_a_list)

## Multiply all the nums present in a list
lambda_multiply_two_nums = lambda num1, num2 : num1 * num2
product_of_a_list = functools.reduce(lambda_multiply_two_nums, list_x)
print(product_of_a_list)


## How to use filter()

seq = [1,2,3,4,5,6,7,8,9,10]

# Filter out the even nums from seq
lambda_check_even = lambda num : 1 if num % 2 == 0 else 0
result = filter(lambda_check_even, seq)
print(list(result))