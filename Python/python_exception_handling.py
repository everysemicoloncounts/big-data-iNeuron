## How to handle exceptions in python

# a = 1
# print(a/0)

# print("Hello")

# list_a = [1,2,8,1,30]
# print(list_a[7])

# a = 5
# try:
#     result = a/0
#     print(result)
# except:
#     print("Some error has occured!!")

# print("Bye")


## Use of else block

# if try doesn't throws an error, then and then only the control goes to else block.
a = 5
try:
    result = a/2
except Exception as err:
    print(err)
else:
    print(result)


## use of finally keyword
# It doesnt matter what happens in try - except - else block, finally code block is always executed.
a = 5
try:
    result = a/2
except Exception as err:
    print(err)
else:
    print(result)
finally:
    print("Doesnt matter try and catch, i will print my-self.")
