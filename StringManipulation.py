from tkinter.tix import InputOnly

s1 = "Hello World1"
s2 = "Hello World2"
print(s1+"\n"+s2)
print(s1+"\t"+s2)
print(s1[0])
print(s1[1])
print(s1[-1])
print(s1[::-1])
print()
print(s1[1:3])
words = ["Hello", "World"]
joined_string = "".join(words)
print(joined_string)

# this is the single line comment
# name = input("what is ur name\n")
# print(len(name))
# test = name+'sabari'
# print("hello " + test)
#

name = "Alice"
age = 30
formatted_string1 = "My name is %s and I am %d years old." % (name, age)
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
formatted_string3 = f"My name is {name} and I am {age} years old."
print(formatted_string1)
print(formatted_string2)
print(formatted_string3)

#Identity Operators
a = 100
b = 100
print(a is not b)
print(a==b)
print(a is b)
print(id(a))
print(id(b))

print("---Identity Operators--")
a=6
print(id(a))
a=6.0
print(id(a))

print('Membership Operators')
p= [1,10,2,-2]
print(10 in p)
print(6 in p)

str="test1"
print("w" in str)
print("e" in str)
print("E" in str)

