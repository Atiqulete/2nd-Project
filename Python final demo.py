# a= 'I LOVE BANGLADESH'
# print(a)
# Syntax is rules of pythone writing (Statements, indentation, comments)
# A=Variables,zero,case sensitive and special character are not allowed , I LOVE BANGLADESH = Statements
# comments=  use in # for th futures plan for editing data
# if 5 > 2:
#     print("Five is greater than two")
# indentation= using the next line has been set as 4 space autometicaly 

# Data type=

# Text Type:str
# x = 'I LOVE BANGLADESH'
# print(type(x))

# Numeric Types:int, float, complex
# int
# x = 10
# print(type(x))

# float
# x = 10.5
# print(type(x))

# complex
# x = 10j
# print(type(x)
      
#  Sequence Types:list, tuple, range
#  list
# x = ["apple", "banana", "cherry"]
# print(type(x))

# tuple
# x = ("apple", "banana", "cherry")
# print(type(x))

# range
# x = range(10)
# print(type(x))

#  Mapping Type:dict
# x = {"name" : "John", "age" : 36}
# print(type(x))

#  Set Types:set, frozenset
# set
# x = {"apple", "banana", "cherry"}
# print(type(x))

# frozenset
# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))

# Boolean Type:	bool
# x = True
# print(type(x))

# Binary Types:	bytes, bytearray, memoryview
# bytes
# x = b"Hello"
# print(type(x))

# bytearray
# x = bytearray(5)
# print(type(x))

# memoryview
# x = memoryview(bytes(5))
# print(type(x))

# None Type:NoneType
# x = None
# print(type(x))

# pythone casting (From input of user)
# a = int(input())
# b = int(input())
# print(a + b)

# a = int(input())
# b = int(input())
# print(a - b)

# a = float(input())
# b = float(input())
# print(a + b)

# a = str(input())
# b = str(input())
# print(a + b)

# Strings Python (Using for multipul line for a varible-('''    '''') ( """"     """"))
# Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
 
# a = '''lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a.capitalize())                    for fast lattet capital

# a = '''lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a.upper())                                   For all upper caseh

# a = '''lorem ipsum Aolor sit amet,
# consectetur adipiscing elit,
# sed do eiUsmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a.lower())                                  For all lower case

# Accessing value and updating string
# a= 'I LOVE BANGLADESH'

# Slicing Strings
# a = "I LOVE BANGLADESH"
# print(a[2:5])

# a = "I LOVE BANGLADESH"
# print(a[-5:-2])

# print(a[10]) 

# a= 'I LOVE BANGLADESH'
# print(a[:10]) 

# a= 'I LOVE BANGLADESH'
# print(a[-10:]) 
 
# a = "I LOVE BANGLADESH"
# print(len(a))

# Modify Strings
# a = "I LOVE BANGLADESH"
# print(a.upper())

# a = "I LOVE BANGLADESH"
# print(a.lower())

# a = "I Love banglades"
# print(a.title())

# a = "I lOVE bANGLADESH"
# print(a.swapcase())

# a = " I LOVE BANGLADESH "
# print(a.strip()) # returns "BANGLADESH"

# a = "BANGLADESH"
# print(a.replace("H", "A"))

# a = "Hello                       BANGLADESH"
# print(a.split(",")) # returns ['Hello', ' BANGLADESH']

# a = "I LOVE BANGLADESH"
# b= a.split()
# print(b[2])

# Concatenate Strings
# a = "I LOVE"
# b = "BANGLADESH"
# c = a + b
# print(c)

# a = "I LOVE"
# b = "BANGLADESH"
# c = a + " " + b
# print(c)

# String Format
# a= input("Enter Your Age : ")
# b = input("Enter Anti's Age : ")
# c = input("Enter Uncle Or Aunt")
# print("my{c} Age is "+a)
# print("my {} Age is {}".format(c,a)")
# Print(f"my {c}" Age is {a})

# Escape Character
# String Methods

# Python Booleans
# Booleans represent one of two values: True or False.

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 500
# b = 100
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(20))

# x = "Hello"
# y = 25
# print(bool(x))
# print(bool(y))

# Python Operators
# print(10 + 5)
# print(10 - 5)
# print(10 / 5)
# print(10 * 5)


# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Arithmetic Operators
#  + Addition ,x + y
# x = 5
# y = 3
# print(x + y)


# - Subtraction, (x - y)
# x = 5
# y = 3
# print(x - y)

# * Multiplication, x * y
# x = 5
# y = 3
# print(x * y)

# / Division, x / y
# x = 5
# y = 3
# print(x / y)

# % Modulus, x % y
# x = 75
# y = 2
# print(x % y)

# ** Exponentiation, x ** y
# x = 2
# y = 5
# print(x ** y) #same as 2*2*2*2*2

# # // Floor division, x // y
# x = 15
# y = 2
# print(x // y)
#the floor division // rounds the result down to the nearest whole number

# Python Assignment Operators
# = ,Operator
#  x = 5, X=5
# x = 5
# print(x)

# += ,Operator
# x += 3
# x = x + 3
# x = 5
# x += 3
# print(x)

# -= ,Operator
# x -= 3
# x = x - 3
# x = 5
# x -= 3
# print(x)

# *= ,Operator
# x *= 3
# x = x * 3
# x = 5
# x *= 3
# print(x)

# /= ,Operator
# x /= 3
# x = x / 3
# x = 5
# x /= 3
# print(x)

# %= ,Operator
# x %= 3
# x = x % 3
# x = 5
# x%=3
# print(x)

# //=  ,Operator
# x //= 3
# x = x // 3
# x = 5
# x//=3
# print(x)

# **= ,Operator
# x **= 3
# x = x ** 3
# x = 5
# x **= 3
# print(x)

# &= ,Operator
# x &= 3
# x = x & 3
# x = 5
# x &= 3
# print(x)


# |= ,Operator
# x |= 3
# x = x | 3
# x = 5
# x |= 3
# print(x)

# ^=  ,Operator
# x ^= 3
# x = x ^ 3
# x = 5
# x ^= 3
# print(x)

# >>= ,Operator
# x >>= 3
# x = x >> 3
# x = 5
# x >>= 3
# print(x)

# <<= ,Operator
# 	x <<= 3
# x = x << 3
# x = 5
# x <<= 3
# print(x)

# Python Comparison Operators
# Equal (==) ,(x == y)
# x = 15
# y = 10
# print(x==y)

# Not equal(!=), (x != y)
# x = 15
# y = 10
# print(x != y)

# Greater than (>), (x > y)
# x = 15
# y = 10
# print(x > y)

# Less than (<), (x < y)
# x = 15
# y = 10
# print(x < y)

# Greater than or equal to (>=), (x >= y)
# x = 15
# y = 10
# print(x >= y)

# Less than or equal to (<=), (x <= y)
# x = 15
# y = 10
# print(x <= y)

# Python Logical Operators
#  and 
# Returns True if both statements are true
# x < 5 and  x < 10

# x = 5
# print(x > 3 and x < 10)

# or
# Returns True if one of the statements is true
# x < 5 or x < 4
# x = 5
# print(x > 3 or x < 4)

# not
# Reverse the result, returns False if the result is true
# not(x < 5 and x < 10)
# x = 5
# print(not(x > 3 and x < 10))

# Python Identity Operators
# is
# Returns True if both variables are the same object
# x is y

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is z)
# # returns True because z is the same object as x
# print(x is y)
# # returns False because x is not the same object as y, even if they have the same content
# print(x == y)
# # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not
# Returns True if both variables are not the same object
# x is not y

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is not z)
# # returns False because z is the same object as x
# print(x is not y)
# # returns True because x is not the same object as y, even if they have the same content
# print(x != y)
# # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


# Class5
 
# a="bangladesh"
# print(len(a))
# print(a.index("B"))
# print(a.find("l"))
# print(a.replace('B','M'))
# b= a.ljust(20)
# print(b,'This is my country.')
# print(a.title())
# print(a.istitle()) 

# Arithmetic operators
# x=10
# y=15
# print(x+y)

# Vag sesh dekhabe 
# x=189
# y=10
# print(x%y)

# Squer
# x=3
# y=2
# print(x**3)

# vag shesh dekhabe na
# x=10
# y=3
# print(x//3)

# Assignment operators
a = 10
# a= a+2
# a+= 2
# a-= 2
# a*= 2
# a/= 2
# print(a)
 
# Comparison operators
# false (a and b er soman na)
# a = 10
# b =20
# print(a==b)

# true (a and b er man soman)
# a = 10
# b =10
# print(a==b)

# true( a not =b , mane a er man b er soman na)
# a = 10
# b =20
# print(a!=b)  

# false ( a er man b theke boro othoba soma)
# a = 10
# b =20
# print(a>=b)   

# a = 10
# b =20
# print(a<=b)

# Python Logical
# and ( gotonar 2 sotti hole true , gotonar 2 tar ekta mitha hole mitha hole mitha)
# a = 10
# b = 20 
# print(a<5 and a>5)

# or ( gotonar 2 tar ekta sotto holei -true)
# a = 10
# b = 20 
# print(a<5 or a>5 )

# not ( mitha gotonar age jodi not bosiye deoya hui tahole mitha gotonao sotto huiye zai)
# a = 10
# b = 20 
# print(not(a<5) and a>5 )
# print(not(a<5))

# Identity Operators
# False (a er b 2ta ek na , tai false)

# a=10
# b=20
# print(a is b) 

#true
# a=10
# b=20
# print(a is not b)


#  Membership Operators
# a = "Bangladesh"
# print("B" in a)

# a = "Bangladesh"
# print("B" not in a)

# Bitwise Operators (No need right now)
# AND & ,  OR| , XOR ^ ,  NOT~ , Zero fill left shift <<, >> Signed right shift

# Conditions and If statements
# a = 10
# b = 20
# if a==b:
#     print('thik ache')
# elif a<= b:
#     print("Ami E1 if")

# elif a>= b:

#     print("2nd E1 if")

# else:
#     print('thik nai')

# Bangla = int(input())

# if Bangla == 80 :
#     print("A+")
# elif Bangla == 70 :
#     print("A")
# elif Bangla == 60 :
#     print("B")

# else: 
#     print("Fail")

# Bangla = int(input())
# if Bangla >= 80 :
#     print("A+")
# elif Bangla >= 70 :
#     print("A")
# elif Bangla >= 60 :
#     print("B")

# else: 
#     print("Fail")



# list

# x = "Bangladesh" ,12
# print(x)


# x = "Bangladesh" 
# print(x)

# x= [12,"Bangldesh",10.2,"india",40]
# print(x)

# x= [12,"Bangldesh",10.2,"india",40]
# print(x[2])

# x= [12,"Bangldesh",10.2,"india",40]
# print(x[0],x[1],x[2],x[3],x[4])


# x= [12,"Bangldesh",10.2,"india",40]
# for i in x:
#     print(i)

# x= [12,"Bangldesh",10.2,"india",40]
# for i in range(len(x)):
#     print(i)

# x= [12,"Bangldesh",10.2,"india",40]
# for i in range(len(x)):
#     print(x[i])

# x= [12,"Bangldesh",10.2,"india",40]
# for i in range(len(x)): 
#     print(i,x[i])

# x= [12,"Bangldesh",10.2,"india",40]
# print(x[0:2])

# x= [12,"Bangldesh",10.2,"india",40]
# x.append("apple")
# print(x)


# x= [12,"Bangldesh",10.2,"india",40]
# x.remove(12)
# print(x)

# x= [12,"Bangldesh",10.2,"india",40]
# x.pop(1)
# print(x)

# x= [12,"Bangldesh",10.2,"india",40]
# x.clear()
# print(x)


# x= ["12","Bangldesh","10.2","india","40"]
# x.insert(2,"Apple")
# print(x)

# x= ["12","Bangldesh","10.2","india","40"]
# print(x.index("Bangldesh"))

# x= ("12","Bangldesh","10.2","india","40")
# y = x.count("Bangladesh")
# print(y)

# x = (10,10,10,10)
# y = list(x)
# z = y.append("Dhaka")
# print(y) 

# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# print(x)

# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# x.update({"Food" : " Banana"})
# print(x)


# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# x.pop("city")
# print(x)  



# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# x.clear()
# print(x)  


# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# print(x.keys())  


# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# print(x.values()) 


# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}
# x.update({"Date": "24/02/2024"})
# print(x)
 

# x ={"Model": 100 ,"Date": "21/02/2023","city" : "daka"}

# for i in x.keys():
#     print(i)


# x = ['a','b','c']
# y = [10,23,34]
# t = dict(zip(x,y))
# print(t)


# set
# a = {"Apple", "Mango", "Orange"}
# print(a)


# a = {"Apple", "Mango", "Orange"}
# for i in a:
#     print(i)

# a = {"Apple", "Mango", "Orange"}
# for i in a:
#     print(i)

# a = {"Apple", "Mango", "Orange"}
# a.add("Banana")
# print(a)

# a = {"Apple", "Mango", "Orange"}
# b = {"Apple", "Mango", "Orange","papaya"}
# c = a.intersection(b)
# print(c)

# a = {"Apple", "Mango", "Orange"}
# b = {"Apple", "Mango", "Orange","papaya"}
# c = a.union(b)
# print(c)

# a = {"Apple", "Mango", "Orange","papaya"}
# b = {"Apple", "Mango", "Orange"}
# c = a.difference(b)
# print(c)

# a = {"Apple", "Mango", "Orange"}
# b = {"Apple", "Mango", "Orange","papaya"}
# c = a.update(b)
# print(c)

# a = {"Apple", "Mango", "Orange",}
# a.clear()
# print(a)

# a = {"Apple", "Mango", "Orange"}
# b = {"Apple", "Mango", "Orange","papaya"}
# c = a.symmetric_difference(b)
# print(c) 

# a = {"Apple", "Mango", "Orange"}
# a.discard("Mango")
# print(a) 


# Python Functions

# def myfunction(x,y):
#     print(x + y)
# myfunction(20,10)

# def myfunction(x,y):
#     print(x + y)
# myfunction(20,10)

# x = lambda a,b: a + b
# print(x(10,12))

# a = lambda x,y : print(x * y)
# a(20,30)

# def abcd(n):
#     if(n > 0):
#         a = n+abcd(n-1)
#         print(a)
#     else:
#         a = 0
#     return a
# abcd(10)


# def myfunction (x,y):
#     return x + y
# print(myfunction(10,20))

# def myfun(n):    next clss
#     for i in range(1, n+1):
#         if n >= 10:
#             print(i)
#             return
# print(myfun(9))
