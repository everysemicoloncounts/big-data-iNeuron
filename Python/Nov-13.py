## Python Dictionary
dict1 = {}
print(type(dict1))

# Insert values in dictionary
dict2 = {}
dict2['name'] = "abc"
dict2['age'] = 13
dict2['skills'] = ["C/C++", "Python", "ReactJS", "Material UI", "Redux", "Golang"]
dict2['states_visited'] = ["Goa", "TN", "UP","Bihar","Jharkhand","Kerala","Karnataka","Haryana","Delhi"]

dict3 = {"color":"Black", "Rent": 7000}

dict2["dict3"] = dict3
# print(dict2)

# Print all the keys of a dictionary
total_keys = list(dict2.keys())
print(total_keys)

# print all the values in the dictionary
total_values = list(dict2.values())
print(total_values)

# Looping through the dictionary senario 1:
for key in list(dict2.keys()):
    print(dict2[key])

## Looping through the dictionary senario 2:
for key, value in dict2.items():
    print("Key = ", key, "and corresponding Value is: ", value)

# Deleting Specific key-value pair in a dictionary
del dict2["states_visited"]

print(dict2)


##Check if the given key exists or not
print("name" in dict2) 


### sets in python

# Empty set
set1 = set()
print(type(set1))

set2 = {'monday','tuesday'}
print(set2)

## Converting a list to set
list1 = [1,2,3,4,1,2,3]
set3 = set(list1)
print(type(set3))
print(set3)

## Using the add method to generate the set

set4 = set()
set4.add(1)
set4.add(1)
set4.add(2)
set4.add(2)
set4.add(5)
set4.add(2)

for num in set4:
    print(num)

## Using Update method
temp_list_num = [1,2,1,2,2,3,4,5,5,2,1,3]
set4.update(temp_list_num)
print(set4)

## Set Operations: Union, Intresection, Difference

set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}

# Union operation
print(set_a | set_b)

# Intersection Operation
print(set_a & set_b)

# Difference Operation
print(set_a - set_b)
print(set_b - set_a)

# Comparision in sets

set_x = {1,2,3,4,5}
set_y = {1,2,3,4,5,1,6}

print(set_x == set_y)
