# Normal list defination
list1 = []
for i in range (1, 11):
    list1.append(i)

# using list comprehension

list1 = [x for x in range(1, 11)]
print(list1)

## Notice how clean the code looks using list comprehension

# get a list of all even nums between 1 to 50

list_evens_from_one_to_fifty = [x for x in range(1, 51) if x % 2 == 0]
print(list_evens_from_one_to_fifty)

# given a list, filter all the even nums from that list

given_list_of_nums = [1,2,3,4,5,6,7,8,9,10]
filtered_evens = [x for x in given_list_of_nums if x % 2 == 0]
print(filtered_evens)


# convert all strings to uppercase in a given list

list_of_strings = ["Hi", "HELLO", "bye", "nICe"]

uppercase_list_of_strings = [str.upper() for str in list_of_strings ]
print(uppercase_list_of_strings)

# given a list of posetive and negative nums arrange the posetives before the negatives in the list

given_list_of_nums = [1,-1,2,-5,9,10,-6]
result = [x for x in given_list_of_nums if x >= 0] + [x for x in given_list_of_nums if x < 0]

print(result)