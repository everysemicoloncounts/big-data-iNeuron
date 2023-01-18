# Declare empty list
list = []
print(type(list))

# insert the values in the list
list.append(1)
list.append(2);

list_names = ["pompia", "gourav", "debo", "sumeet"];
list.append(list_names);
list_decimal = [1.2,2.3,3.4,4.5];
list.append(list_decimal);

for num in list:
    print(num);

# Create a list of natural nums from 1 to 1000;
list_one_to_thousand = []
for i in range(1,1001):
    list_one_to_thousand.append(i);

print(list_one_to_thousand)

# calculate the length of a list;
print(len(list_one_to_thousand))

# concatinate two lists:
int_list1 = [1,2,3]
int_list2 = [3,4]

int_list1 = int_list1 + int_list2

print(int_list1)

# Difference between append() and extend()

list9 = [1,2,3];
list10 = ["Hi", "Hello", "bye"]
list9.append(list10);

list11 = [1,2,3];
list12 = ["Hi", "Hello", "bye"]
list11.extend(list12);

print(list9);
print(list11);

# List Slicing
list13 = [20,30,40,50,60,80,90]
#syntax -> list_name[start: end]

print(list13[:])
print(list13[2:6])

# Print the last element of the list
list13 = [1,2,3,4,5,6,7,8,9]
print(list13[-2])

# print list in reverse order
print(list13[-1: :-1])


## Python Strings
str1 = "Hello Pompia"
print(str1)

## Multiple lines as a string
str2 = '''Gourav
is planning
not to attend
the seminar.
'''
print(str2)

## Print each character from the string
for s in str1:
    print(s);

# ## Change the string
# str1[7] = "H"
# print(str1);

### Python Tuples
t1 = ("Gourav", "Pratap",("Hello", "World"),"Gym");
print(t1)

print(t1[0], t1[1])

##Print using loop;
for t in t1:
    print(t)

str14 = "Hello"
str15 = "World"
result = ""

for i in range(0, len(str14)):
    result += str14[i]
    result += str15[i]
print(result)