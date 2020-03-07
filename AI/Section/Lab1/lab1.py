print("Hello, World!")
# print("This is a
# multiline string.")
print("This is a \n multiline string.")
print("""This is a
multiline string.""")

print('-' * 50)
########################################################
# Multiple Assignment
a = b = c = 1
print(a)
print(b)
print(c)
a, b, c = 1, 2, "john"
print(a, b, c)
print(a, b, c, sep='/')
print(a, b, c, end='/\n')
print(a, b, c, sep=',', end='/\n')

########################################################
# Swap
a = 10
b = 15
print(f"a = {a} , b = {b}")
a, b = b, a
print(f"a = {a} , b = {b}")

print('-' * 50)
########################################################
# Casting
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)
x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2
print(x, y, z)
x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)

print('-' * 50)
########################################################
# input
# string 
print("Enter your name:")
name = input()

# int
print("Enter your age:")
age = int(input())

# float
print("Enter your CGPA:")
CGPA = float(input())

print("Hello, " + name + "\nage : " + str(age) + "\nGPA : " + str(CGPA))
print(f"Hello, {name} \nage : {age}\nGPA : {CGPA}")
print("Hello, %s \nage : %d \nGPA : %.2f" % (name, age, CGPA))

print('-' * 50)
########################################################
# Arithmetic Operators
# + - * / % ** //
# **    Exponentiation	x ** y	 
# //	Floor division  x // y
print(5 / 2)  # 2.5
print(5 // 2)  # 2

# Bitwise Operators
# & | ^ ~ << >>
x = 5
y = 2
print(x & y)  # 0
print(x | y)  # 7
print(x ^ y)  # 7
print(~x)  # -6
print(x >> y)  # 1
print(x << y)  # 20

# Assignment Operators
# = += -= *= /= %= //= **=
# &= |= ^= >>= <<=

# Comparison Operators
# == != > < >= <=

# Logical Operators
# and or not
if not (5 < x < 10):
    print("out of range")
x = 1
y = 15
while x <= 7 and y > x:
    print(x, y)
    x += 1
    y -= 1

for i in range(5):  # i = 0 -> 4
    print(i)

for i in range(2, 6):  # i = 2 -> 5
    print(i)

# Identity Operators
# is       Returns true if both variables are the same object
# is not   Returns true if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

print(x == y)
# returns True because x is equal to y


x[0] = "orange"
print(x)
print(z)
z = x[:]
print(x is z)
z[0] = "apple"
print(x)
print(z)

# Membership Operators
# in        Returns True if a sequence with the specified value is present in the object
# not in
print("banana" in x)

print('-' * 50)
########################################################
# String
str = 'Hello World!'

print(str)  # Prints complete string
print(str[0])  # Prints first character of the string (index 0)
print(str[2:7])  # Prints characters starting from index 2 to index 6 ( [2:7) )
print(str[2:])  # Prints string starting from 3rd character
print(str[:2])  # Prints first two characters
print(str * 2)  # Prints string two times
print(str + "TEST")  # Prints concatenated string

a = " Hello, World! "
print(a.strip())  # strip() method removes any whitespace from the beginning or the end
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("l", "J"))
print(a.replace("l", "J", 1))
print(a.split(","))  # returns ['Hello', ' World!']
# split() method splits the string into substrings if it finds instances of the separator
# capitalize() Return a copy of the string with its first character capitalized and the rest lowercased.
s = 'hello'
print(s.capitalize())  # Hello
print(a.count('o'))  # 2
# center(width[, fillchar])
# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
print(s.center(9, '-'))  # --hello--
# find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]
print('abcabca'.find('ab'))  # 0
print('abcabca'.find('ab', 1))  # 3
print('abcabca'.find('ab', 1, 3))  # -1
# index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

########################################################
