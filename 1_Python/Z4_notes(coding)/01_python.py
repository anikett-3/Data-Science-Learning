# NOW WE START LEARNING PYTHON -----

## CHAPTER -1


print("hello")

a = 5
print(a)

instructr = 'risabh mishra'
print('python by ',instructr) #  value of (instructr) hs been print

print('python by   ',instructr, sep='-') # sep keyword use tp seperate sentence

# here instructor or a are VARIABLE (which contain value)

print('5+3') # if we put any value under string it assigned as a STRING

print(5+3)  # otherwise it assigned as your input  


#  VARIABLE

'''variable is like conatiner which store Value
like'''

#   FOR ASSIGNING A VALUE OF WORD OR SENTENCE USE INVERTED COMMA ('')(" ")

a = 5
print (a)  # here a is variable and 5 is value

aman = 22
a = aman    # declare a variable BY USING A VARABLE
print(a)  

x = 8  # adding a no. to a variable
print(x+3) #here python treat vairable as int and add another value in it

# MULTI VARIABLE

P,Q,R = 12,'asdf',3.45
print(P,Q,R)   # multivariable use ,, comma to separate value and  variable

# TYPES OF VAARIABLE or ways to declare variable name
MyName = 'aman' # pascal case   
myName = 'aman' # camel case
myname = 'aman'# flat case
my_name = 'aman' # snake case

## rules to declare a variable 
## 1. variable name must start with ; LETTER OR _ (UNDERSCORE)
## 2. Variable name can contain; LETTER , NUMBER, UNDERSCORE
## 3.  variable names can't be a reserved word

#OR  

print('kaise ho pantar log')  # by single quote

print(" you'r a good person ")  # if single quote is in use in sentence use double qoutes

print(''' you'r a "good" person  ''')   #if singlle or double or only double quote is in use in sentence use triple qoute .


###    ASSIGMENT 1 

# QUE.  -- PRINT - "Quotes" and 'single Quotes' are tricky

print('''"Quotes" and 'single Quotes' are tricky''')   # or

print(" \"Quotes\" and 'single Quotes' are tricky") #or by using \ forward slash(\".....\")



#________________________________________________________________________

## CHAPTER --  2

''' which types of data
store in variable is called data types

likes
'''
#  types of data types 
'''
(1) NUMERIC DATA TYPES
1.1_ int - all integers numbers without decimal
1.2_ float - all integers with decimal
1.3_ complex - complex no. (a+bj form, like a+2b)
'''
#eg

a = 10     # int 
b = 15.238   # float
c = a+4j    #complex

print (a, b, c)

'''OR IF YOU DONT ANY VARIABLE CONTAIN WHICH TYPES OF DATA TYPE 
 THERE IS A FUNCTION IN PYTHON TO DECLARE DATA TYPE '''
 
#  use..  print( type(), type(), type()  )

print(type(a),type(b),type(c))

'''
(2) BOOLEAN DATA TYPES
   TRUE OR FALSE
   
 (3)  NONE DATA TYPE 
 
'''

'''
(4) SEQUENCE DATA TYPES
4.1 STRING
4.2 LIST 
4.2 TUPLE

1 STRING 
text = ('this is string')
string is group of words in under in single '_' or 
double "_" quotation mark with parenthesis ( )
OR string are immutable


2 list 

 list is a data type in which you store 
 group of element in one variable or word bordered
 with quotation mark ' ' under
 all this is in sqaur brace [ ] OR
 item in list is mutable
 
 like
'''
my_list = ['data 1', 'data 2', 'data 3', 234, 9.76]
mine = ['aman', 'kumar']
print (my_list)
print (mine)

'''
3 TUPLE
tuple is also like a list but here we use parenthesis ( )
item in tuple is immuatable

'''
my_tuple = ( "data1", 'data 2', 'data3',234, 9.76, 4+3j)
print(my_tuple)

'''
(5) SET DATA TYPE
5.1 set is like a tuple or list WITH curly braces { } OR
SET (MUTUABLE) [set ke andar data modify kar sakte hai]
OR 
5.2 FROZEN SET (IMMUTABLE)
data ka andar modificiation nhi kar sakte
dono set hi repeated no. print karte
'''
my_set = {'data 1', 'data 2', 'data 3', 234, 9.76, 4+3j} # similar to tuple or list with {}
unique_number = {1,2,3,3,3,4,4,4,5,5} # unique set print repeated value only onw time
print(unique_number)
unique_number1 = frozenset([1,2,3,3,3,4,4,4,5,5])
print(unique_number1)

'''
(6) MAPING DATA TYPE
6.1 - DICTIONARY DATA TYPES --  collection of [KEY-VALUE] pairS
LIKE

'''
person = {'name': 'gopal','age':20, 1000:1000.000
  
}
print(person)

'''
(7) BINARY ;  used too work with binary data. Such as image, audio, mp3 files, etc.

(7.1) BYTES; immutable seqence type to represent seqence of bytes (8-bit values)

(7.2)BYTEARRAY; similar types but can be modified

(7.3)MEMORY VIEW; used to create a "view" of memory containing binary data

'''

byte_1 = b'aman'  # bytes
print(byte_1)

## TYPE CONVERSION

c = '4'
b = '5'
print(c+b)
print(type(c))
print(type(my_list))
print(type(unique_number))
print(type(byte_1))        #etc


### ASSIGMENT

# create a 3 vaiable which store city,name,age

city= 'bhopal'
age= 22
name= 'aniket' 

print(name)
print(age)
print(name)   # or
print(city,age,name) #or
print('my name is', name, 'iam', age,'old', 'i live in' ,city) #OR

# YOU USE FORMATED STRING(F-STRING)  (f"...{}....{}...")                 

print(f"my name is {name} my age is {age} years old and i live in {city} ")

## INPUT FROM USER    .... default input  function take  value as a STRING value in python

a = input()
print(int(a)+int(a))

b = input('entet 1st no.')
c= input('enter 2nd no.')
print(b+c)  # here value treat as string eg. 2+4 = 24
#or
print(f'you sum of {b} and {c} is {int(b)+int(c)}') # here if we use int data type for sum integer value

name1 = input('enter your name: ')
age1 = input('enter your age:  ')
print(f'your name is {name1} you are only {age1} old!')

#OR
print(f'next year you are become {int(age1)+1} year')  #####    {int(.....)+,_....}


#________________________________________________________________________________

# CHAPTER-- 3

## OPERATORS

# 1.. ARTHIMETIC OPERATRS
a = 5
b= 3
print(a+b) #addition 
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) #division
print(a//b)# floor division
print(a%b) # modulus
print(a**b) # square

# 2.. COMPARISON OPERATOR -- OUTPUT IS TRUE OR FALSE

print(a>b) # graeter than
print(a<b)  # less than
print(a==b) # equal to opearotor
print(a!=b) # not equal to

# 3... ASSIGNMENT OPERATOR

c = 19 # assignment oper ( which assign a value in it, like 19 is in C 'variable')

# 4... LOGICAL OPERATOR
# AND    # 3 FALSE , 1 TRUE
print(a>10 and b<10) # one condition  is true and one condition  is false so OUTPUT IS FALSE
print(a<10 and b>10) # one condition  is true and one condition  is false so OUTPUT IS FALSE
print(a>10 and b>10) # both condition  is false so OUTPUT IS FALSE
print(a==5 and b==3) # both condition  is true so OUTPUT IS TRUE

# OR   # 3 TRUE  , 1 FALSE

print(a>10 and b<10) # one condition  is true and one condition  is false so OUTPUT IS TRUE
print(a<10 and b>10) # one condition  is true and one condition  is false so OUTPUT IS TRUE
print(a>10 and b>10) # both condition  is false so OUTPUT IS FALSE
print(a==5 and b==3) # both condition  is true so OUTPUT IS TRUE

# AND & OR RULES
'''
               AND     |  OR
TRUE + TRUE =  TRUE   |  TRUE
FALSE + FALSE= FALSE  |  FALSE
TRUE + FALSE = FALSE |  TRUE
FALSE + TRUE = FALSE |  TRUE 

'''

 # 5 .. IDENTITY  OPERATOR
 
x = [1,2,3,4]
y=x

z = [1,2,3,4]

print(x is y)  # output TRUE because both memory location is same
print(z is x)  #  output FALSE because both variable memory location is different doesnot matter if value is same or not
print(x is not z)  # output is true you know why
 
 ## 6... MEMBERSHIP OPERATOR

my_list = ['orange','apple','mango']

print('apple'in my_list)  # true #ask it kya apple list me hai
print('apple' not in my_list) # false
print('apple222' not in my_list) # true


# 7.. BITWISE OPERATOR
#                     - OR (|) ,, AND(&) ,, XOR(^) ,, NOT (~)

# AND & OR RULES
'''
               AND     |  OR
TRUE + TRUE =  TRUE   |  TRUE
FALSE + FALSE= FALSE  |  FALSE
TRUE + FALSE = FALSE |  TRUE
FALSE + TRUE = FALSE |  TRUE 

'''
# a = 5         # 5 in binary - 0101
# b = 3         # 3 in binary - 0001
                #               0001  ## 0 AND 0 = 0 , 1 AND 0 = 0 , 1 AND = 1 ,,, etc
print(a & b)    # 1 in binary - 0001

print (a|b)     #               0101 which is 3 in binary

#________________________________________________________________________________________________________________

# CHAPTER ---4 

# there are 5 conditional statement in python

# 1.. if statement   ## if only excute only when is true

a = 25
b = 129
if a > b :     # a>b is condition 
    print('a is grater than b')
    
age = 20
if age> 18:
    print('you are adult')
    
# by user input

age1 = int(input('enter your age'))
if age > 18:
    print ('you are adult also')
    

    

# 2.. .. else statement   ## if only excute only when IF condtionion is not valid or FALSE.

aa = 256
bb = 129
if a > b :     # a>b is condition 
    print('a is grater than b.')
else:
    print('b is greater than a.')
    

age2 = int(input('enter your age:'))
if age2 > 18:
    print ('you are adult also')
else :
    print('you are below 18')
    
    
# elif    # elif condition is use when there is multi conndition exist and 1st condition is false.

y = 18
x = 23
if a>b:
    print('a is greater')
elif a==b:
    print('a is equal to b')
else:
    print('b is greater')
    
# by user input

marks = int(input('enter your marks: '))
if marks>=90:
    print('excellent marks :: GRADE A+')
elif marks >= 80:
    print('GRADE A')  
elif marks >= 70:
    print('GRADE B') 
    
elif marks >=60 or marks <= 70:
    print('passing marks :: GRADE C')
else :
    print('fail')
    


#______________________________________________________________________________________________________________________


# CHAPTER --5

## 3... NESTED CONDITION -- NESTED'IF-ELSE'
# multi condition that depend on each other
#-- means -- if else statement UNDER if else statement


# if marks>50:
#     print('good marks: ')
#     if marks>60:
#         print('ggod11')
#     elif marks>65:
#         print('good22')
#     else:
#         print('good33')
# else:
#     print('fail')

### Q . check user input no is positive even/odd or negative
    
number = int(input('enter a number: '))
if number>0: # first check number if no. is positive
    if number%2 == 0:
        print('the number is positive and even')
    else:
        print('the number is positive and odd')
else: # the no. is not positive
    if number== 0:
        print('the number is zero')
    else:
        print('The number is negative')


## 5... CONDITIONAL EXPRESSON
# SYNTAX --- (value)_if_true CONDITION else (value) _if_false

age = 16 # or 
# age1 = int(input('enter your age'))  # by user input
status= "adult" if age>= 18 else "minor"
print (status)



#______________________________________________________________________________________________________________________

# CHAPTER --6

'''  SYNTAX
 def my_function (paramaters):   # here my _funtion of funtion name  we have to declare 
 like any variable               # and we have to call later
    instruction 1               # and parameter is also variable (eg.. a , aman_2, num1, user_name)
    instruction 2               # parameter separate with (,) comma
    
    
    return result          # here we call the funtion name / variable



'''
# eg''1
#or define function
def greeting():
    print('good morning')
    
    
# use or call function 
greeting()


#..2 
# funtion to add two numbers and print arguments

def add2no(a,b):
    result = a+b
    print('the sum is:', result)
    
# call above function 
add2no(5,6)  # arguments (5,6)  and call fun

# or
add2no(a=4, b=7) # it also call funtion
# or
add2no(b=8, a= 34) # it also call function





###   RETURN STATEMENT  ###


def addnum(a,b):
    return a+b
   # return a-b  # NOTE-- after return statement function end
sum = addnum(123,7)
print(sum)

### Q.1
''' FUNTION TO CONVERT CELSIUS TO FAHRENHEIT
''' #  by using return functiom
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

# call function
temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print('with return',type(temp_f))



## by using WITHOUT RETURN statement
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    print(fahrenheit)

# call function
#celsius_to_fahrenheit(25)
temp_f2 = celsius_to_fahrenheit(25)
print('without return',type(temp_f2))

'''NOTE
return ham use karte hai qk uski data type pata
chale or ham usse futurr me use kar sake futher oprearion 
ke liye ORRR without return value NONE TYPE ho jati ho'''



### PASS STATEMENT ###

''' NOTE 
PASS ham tab use karte jab hame at that time
fuction,loop, etc usme hame value assign nhi karna chahte 
or nhi koi operation perform karna chahte'''

def use_pass():
    pass
# code to be updated later

print('helooooo')

#________________________________________________________________________________________________________________________________________

# CHAPTER --7 

### Argument in function ###
''' NOTE ,, there are 4 types of arguments can pass
at the time of function call.
1. required arguments(single,/ multiple arguments)
2. Default arguments
3. Keyboard arguments (name arguments)
4. Arbitrary arguments (variable - lenght arguments (*args))


'''

# 1. Required Arguments   (single / / multiple)

def greetings(name):
    print('hello', name , '!')
    
greetings('aman')     ## aman is arguments
# greetings(NEED ARGUMENTS!!!)               ## required an argument to run code

def intro(course_name, instructor_name):
        print('welcome to ', course_name, 'course by', instructor_name)
intro('python', 'risabh')


### 2.. DEFAULT ARGUMENTS ###
def greet(name='worldd'):
     print('hello,',name,'!')
     
greet()      ## fun call by greet but WITHOUT argument
            ## the output is -- hello, worldd !
#NOW 

greet('amann') #here argu is (aman) so 

# outut is -- hello, aman !


        
## 3.. KEYBOARD ARGUMENTS##
'''WHEN CALLING YOU SPECIFY ARGUMENTS BY THE PARAMETERS NAME
'''
def divide(a,b):
    return a/b
result = divide(b=10, a=20)  # with keyboard argument
print(result)   # output : 2.0

result_1 = divide(10,20)   # with positional argument
print(result_1)   # output : 0.


## 4.. ARBITRARY ARGUMENTS (*args)
'''NOTE
If you're unsure how many arguments will be passed, use *args to accept any number of
positional arguments.
Purpose:- Allows you to pass a variable number of positional arguments.
Type:- The arguments are stored as a TUPLE.
Usage:- Use when you want to pass multiple values that are accessed by position.
'''  #  argument stored as a TUPLE
## 4.1 # arbitrary positional arguments

def add_num(*args):
    return sum(args)
# any numbers of arguments
result = add_num(1,2,3,4,5,6)  # numerous variable have passed
print(result)   # output is : 21


def add_no(*args):
    print(type(args))  ## TUPLE
    return sum(args)
op = add_no(1,2,3,4) # variable no. of arguments
print(op)
print(type(op))


def wel(*names):
    for name in names:
        print(f'hello, {name} !')
        
wel('madhav','aman', 'abhishek')



### 4.2 .. Arbitrary Keyword Arguments (**kwargs)
'''NOTE
If you want to pass a variable number of keyword arguments, use **kwargs.
Purpose:- Allows you to pass a variable number of keyword arguments (arguments with
names).
Type:- The arguments are stored as a dictionary.
Usage:- Use when you want to pass multiple values that are accessed by name.
''' # VALUE STORED AS DICTIONARY

def print_details(**kwargs):
    print(type(kwargs))     # dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_details(name="Madhav", age=26, city="Delhi")
print_details(name="Madhav", age=26)  # kitne v arguments with keyword de sakte hai

# Output:             
# name: Madhav                  # name: Madhav
# age: 26                       # age: 26
# city: Delhi





# eg2

def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")
    
# multiple keyword arguments
shopping_cart(apple=15, orange=12, mango=10)

# # Output:
# Items Purchased:
# apple: ₹15
# orange: ₹12
# mango: ₹10
# Total: ₹37


#  NOTE  -- single star ( * ) -- args (positional arguments)
#           double star ( ** ) -- kwargs (keywords arguments)


# Q1: Convert a list of integers to strings using map().

nums = [10, 20, 30]

result= map(str,nums)
print(list(result))



#2.. Double the values using map() and a lambda:


# def square(n):
#     return n*n

# nums = [1, 2, 3, 4]
# result = map(square,nums)
# print(list(result))



#Q3: Write a function square() that squares a number. Use map() to apply it to a list of numbers.

def square(x):
    return x*x

nums1 = [2, 3, 4]
result= map(square,nums1)
print(list(result))



# CHAPTER --- 8

### STRINGS  ###

n = 'aman'
print(n)
print(type(n))    # string

'''  A string is a sequence of characters. 
In Python, strings are enclosed within single (') or
double (") or triple (""") quotation marks. '''

#Examples:
print('Hello World!') # use type() to check data type
print("Won’t Give Up!")
print("\"Quotes\" and 'single quotes' can be tricky.")

## Types of Function Arguments. #

'''  A formatted string in Python is a way to insert variables or expressions inside a string. It
allows you to format the output in a readable and controlled way.
There are multiple ways to format strings in Python:

1. Old-style formatting (% operator)
2. str.format() method
3. F-strings (formatted string literals)
'''

## 1..  Formatted String - % Operator
'''
Old-style formatting (% operator)
This approach uses the % operator and is similar to string formatting in languages like C.

NOTE -- Syntax: "string % value"  '''

name = "Abhishek"
age = 17
print("My name is %s and I’m %d." % (name, age))
# %s, %d are placeholders for strings and integers


## 2...  Formatted String - str.format()

'''   str.format() method
In Python 3, the format() method is more powerful and flexible than the old-style %
formatting.

NOTE - Syntax: "string {}".format(value)  '''

name1 = "Madhav"
age1 = 16
print("My name is {} and I’m {}.".format(name1, age1))

# You can also reference the variables by index or keyword:

print("My name is {0} and I’m {1}.".format(name1, age1))
print("My name is {1} and I’m {0}.".format(name1, age1))



#OR -- WE use without declare ay variable to print statement by  - (str.format)  like

print("My name is {name11} and I’m {age11}.".format(name11="Mufasaa", age11=28))




## 3... Formatted String – F-strings

'''  F-strings (formatted string literals)
In Python 3.6, F-strings are the most concise and efficient way to format strings. You
prefix the string with an f or F, and variables or expressions are embedded directly within
curly braces {}.

NOTE -  Syntax: f"string {variable}"  '''

name3 = "karan"
age3 = 19
print(f"My name is {name3} and I’m {age3}.")

# You can also perform expressions inside the placeholders:

print(f"In 5 years, I will be {age3 + 5} years old.")

# in f-string we also perform an operation.




### ESCAPE CHARACTER ## 

''' escape character is a backslash \ followed by the character you want to insert.
NOTE - \n = for new line
      \t = for  new tab    '''

#  backslash with character 
print('Hello\nWorld!') # \n for new line
print('Hello\tWorld!') # \t for tab


# print single and double quotes

print(''' "imagin you are in IES" ''') # if we want to use ".." then use under  ''' ... ''' (triple)
print(" \"imagin yor are im ICOT\" ") # OTHERWISE YOU USE \".......\" 
print("  \"Quotes\" and 'single quotes' can be tricky. ")









###    OPERATION IN STRING    ###


a = 'Hello'
b = 'pantar log'

print(a+b)     #  1. CONCATENATE (Add two string value)

print(a*2)   # 2.. multiply n times  a value of string  



if 'H'in a :   # 3.. MEMBERSHIP (in) operator
      print('yes')
else:
      print('no')
      
      
if 'xyz' not in a :   # 3.. MEMBERSHIP (not in) operator
      print('yes')
else:
      print('no')
      
      

print("hello\nworld")


print(r"hello\nworld")   # r = Raw string (suppress the escape character)

# raw string syntax --- print(r'...\n....')...\n


# __________________________________________________________________________________

# CHAPTER 8.2 

### String Indexing ##  [ ]
'''You can access individual characters in a string using their index.
Python uses zero-based indexing. meaning first characeter has in index of zero (0). 
NOTE - SYNTAX ==   string[index_value]'''

name = 'aniket kumar '

print(name[0]) # a
print(name[3]) # k
print(name[7]) # k

    # eg            # -12-11-10 -9 -8 -7  -6 -5 -4 -3 -2 -1  (negative indexing)
                    #  a  n  i  k  e  t       k  u  m  a  r
                    #  0  1  2  3  4  5   6   7  8  9  10  11 (positive indexing)

# reverse indexing
print(name[-5]) # u
print(name[-1]) # space  (blank space also count in string)
print(name[-2]) # r



### STRING SLICING #
''' String slicing
allows you to get subset of characters from
a string using a specified range of indices.
NOTE - Syntax: 
                string[start : end : step] 

• start : The index to start slicing (inclusive). Default value is 0.
• end : The index to stop slicing (exclusive). Default value is length of string.
• Step : How much to increment the index after each character. Default value is 1.
'''

name1 = "MADHAV"
print(name1[0:2])     # 'MA'
 
print(name1[0:5:2])   #'MDA' # skip one value # FOR (2).. ALETRNAATIVE VALUE IN USE

print(name1[2:5:1])   # 'DHA' (PUT 2nd alternate value)

print(name1[0:5:3])   # MH (put 3rd alternate value)

print(name1[0:5:4]) #  MA  (PUT 4TH ALTERNATE VALUE)

print(name1[1:4])# senond to fourth chr
print(name1[-1])    # last chracter
print(name1[:-1])   #  except last char print all
print(name1[-1:])   # last char
print(name1[5:])    # last char
print(name1[-2:])    # last two char
print(name1[-3:])   # last three char
print(name1[0::2])   #every senod chara
print(name1[:])   # all char
print(name1[::])    # all char
print(name1[::1])  # all char from starting

# reverse string

print(name1[::-1]) # all char with reverse way
print(name1[::-2])  # alternate from reverse




### STRING METHOD ###

word = 'hello bhai , log hello'

#1. len()
print(len(word))    # count char in string (space also count)

#2.upper
print(word.upper())    # convert all char in upper case

#3. lower()
print(word.lower())  # convert all char in lower case

#4. count()
print(word.count('l'))  # count times specific char

#5. find()
print(word.find('e',))

#6.split()
print(word.split(','))

#7. replace()
print(word.replace('bhai', 'pantar'))

#8. title ()
print(word.title())


#9. strip()

word2= '  hello world  '

print(len(word2))

print(word2.strip())

zwords = ('madhav', 'is', 'great')
print(" ".join(zwords))
print("-".join(zwords))


#______________________________________________________________________________________________________________________________


# CHAPTER -- 9

# ## LOOPS ##
# ''' Loops enable you to perform repetitive tasks efficiently without writing
# redundant code. They iterate over a sequence 
# (like a list, tuple, string, or range) or execute a
# block of code as long as a specific condition is met.'''

# ## 3 TYPES OF LOOPS 

# #1.. WHILE LOOPS ##
# '''The while loop repeatedly executes a block of code as long as a given condition remains
# True. It checks the condition before each iteration.

# NOTE - SYNTAX ---  while condition:
#                        # Code block to execute
# '''
# couunt = 0
# while couunt <4:  # check condition
#     print(couunt)
#     couunt += 1
    
    
# ## ELSE STATEMENT  ##
# '''An else clause can be added to loops. It executes after the loop
# finishes normally (i.e., not terminated by break).'''

# count = 3
# while count > 0: # Condition
#     print("Countdown:", count)
#     count -= 1
# else:
#     print("Liftoff!") # Run after while loop ends
    
# ## while True:
#     #print('lund lelee') # while run always when condition is true

# # check condition whenn usin while loop to avoid INFINTE LOOP


# # 2.. FOR LOOP  ##
# '''The for loop in Python is used to iterate
# over a sequence (such as a list, tuple, dictionary,
# set, or string) and execute a block of code
# for each element in that sequence.
# NOTE-- SYNTAX -- for variable in sequence  '''

# language = 'python'
# for x in language:
#     print(x)    # out - p y t h o n
    

# ## RANGE () FUNCTION ##
# '''To repeat a block of code a specified number 
# of times, we use the range() function.
# The range() function returns a sequence of
# numbers, starting from 0 by default,increments by 1
# (by default), and stops before a specified number.

#  NOTE - Syntax:
#       #  range(stop)
#       #  range(start, stop)
#        #  range(start, stop, step)
# • start: (optional) The beginning of the sequence. Defaults is 0. (inclusive)
# • stop: The end of the sequence (exclusive).
# • step: (optional) The difference between each number in the sequence.
# Defaults is 1.

# '''
# # Example1: Basic usage with One Argument - Stop

# for i in range(5):
#     print(i)                    # Output: 0 1 2 3 4




# # Example2: Basic usage with Start, Stop and Step

for i in range(1, 10, 2):   
    print(i)                # Output: 1 3 5 7 9

print(' ')

for i in range(6):
    print(i)
else:
    print('for looop ended')
    
    
    
# ## ** LOOP CONTROL STATEMENT **  ##
# '''Loop control statements allow you to alter the normal flow of a loop.
# Python supports 3 clauses within loops:

# • pass statement
# • break Statement
# • continue Statement
# '''
# # PASS STATEMENT
# ''' The pass statement is used as a placeholder (it does nothing) for
# the future code, and runs entire code without causing any syntax error.
# '''

# for i in range (5):
#     # code to be updated later
#     pass                        # no output but run



# ## BREAK STATEMENT
# '''The break statement terminates the loop entirely, exiting from it
# immediately.
# '''
# for i in range (5):
#     if i == 3:
#         break           # (the loop terminated when condition met true for i == 3)
#     print(i)            # output -- 0 1 2 


# print('__')

# ## CONTINUE STATEMENT #
# ''' The continue statement skips the current iteration and moves
# to the next one.
# '''
# for i in range(5):
#     if i == 3:
#         continue        # (the loop skips when condition met true for i == 3)
#     print(i)            # Output: 0 1 2 4
    
    
# ## break vs continue Statement  #

# # pass statement

# countt = 5
# while countt > 0:
#     if countt == 3:
#         pass
#     else:
#         print(countt)
#     countt -= 1
# # Output: 5 4 2 1



# # continue statement: don't try - infinite loop

# # count = 5
# # while count > 0:
# #     if count == 3:
# #         continue
# #     else:
# #         print(count)
# #      count -= 1
# # Output: 5 4 3 3....... infinte

# # continue and break has are look like same but both are different to 
# # each other , like above eg both code are a same but difference is when
# # we use PASS it skio that value and else condition but compile last condition
# # (count =+ 1) this one so value is itrate and 
# # continue statement ignore all avlue after continue key and print last value infintly



# # NOTE -- QUE..
# ## ** CONTROL INFINITE LOOP IN USER INPUT ## 
 
 
# # while True:
# #     user_input = input("enter 'exit' to STOP:: ")
# #     if user_input == 'exit':
# #         print("congrtas ! ypu gussed it right")
# #         break
# #     print("sorry , you entered :", user_input)
# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print(j,end="")
#         j=j+1
#     i=i+1
#     print(" ")



## 3.. NESTED LOOP ##
''' Loop inside another loop is nested loop. This means that for every single time the outer
loop runs, the inner loop runs all of its iterations.

NOTE - Why Use Nested Loops?
• Handling Multi-Dimensional Data: Such as matrices, grids, or lists of lists.
• Complex Iterations: Operations depend on multiple variables or dimensions.
• Pattern Generation: Creating patterns, such as in graphics or games.

NOTE - Syntax:

Outer_loop:
    inner_loop:
        # Code block to execute - inner loop
# Code block to execute - outer loop

'''
# print numbers from 1 to 3:

for num in range (1,4):  # simply we have to write this code for 3 times to execute
    print(num)
    
# but in nested loop --

for i in range(3):
    for num in range(1,4):
        print(num)
    print('_ _')
    
'''pehele outer loop run hoga or inner loop apna itration poora karega 
then fir outer lopp chalega then fir inner lopp chalega
then fir outer lopp chalega jab tak 3 na aajay'''


for i in range(3):
    print('outer loop iteration no, ',i )
    for num in range(1,4):
        print(num)
    print('_ _')


## WHILE LOOP (NESTED)
i = 1
while i < 4:
    print("while loop itration no,", i)
    for j in range(1,4):
        print(j)
    print("-")
    i +=1
        
## QUE. print a prime no. between range of 2 to 10 using nestes loop:

for num in range(2,10):
    for i in range (2, num):
        if num % i == 0:
            break
    else:
        print(num)
            
#______________________________________________________________________________________

# CHAPTER -- 10 

## LIST IN PYTHON ***

'''
A list in Python is a collection of items (elements) that are ordered, changeable
(mutable), and allow duplicate elements.
Lists are one of the most versatile data structures in Python and are used to store
multiple items in a single variable.
Example:  '''

# fruits1 = ["apple", "orange", "cherry", "apple"]
# print(fruits1)   # # Output: ['apple', 'orange', 'cherry', 'apple'] 

# print(type(fruits1))  # sh00w the data type of fruits 



##  1. Create List in Python ## 

''' 
You can create lists in Python by placing COMMA - SEPARATED values between 
square brackets [].
Lists can contain elements of different data types, including other lists.

NOTE -- Syntax: list_name = [element1, element2, element3, ...]  '''

# # List of strings
# colors = ["red", "green", "blue"]
# # List of integers
# numbers = [1, 2, 3, 4, 5]
# # Mixed data types
# mixed = [1, "hello", 3.14, True]
# # Nested list
# nested = [1, [2, 3], [4, 5, 6]]


### 2.. Accessing List Elements - INDEXING
'''
You can access elements in a list by referring to their index. Python uses zero-based
indexing, meaning the first element has an index of 0.

NOTE --   Syntax: list_name[index]
Example: '''

#INDEX =    0         1       2          3         4       # POSITIVE INDEX
fruits = ["apple", "orange", "cherry", "apple", "mango"]
#            -5      -4          -3       -2     -1        # NEGATIVE INDEX

# # Access first element
# print(fruits[0]) # Output: apple

# # Access third element
# print(fruits[2]) # Output: cherry

# # Access last element using negative index
# print(fruits[-1]) # Output: mango



### 3. LIST SLICING  #
'''Slicing allows you to access a range of elements in a list. You can specify the start and
stop indices, and Python returns a new list containing the specified elements.

NOTE -- Syntax: list_name[start:stop:step]'''  # start is include / but not stop(stop-1)
                                            # default start value is 0 and stop value is -1(last one) {index}
numbers = [10, 20, 30, 40, 50, 60 ,65,75,89]

# # Slice from index 1 to 3
# print(numbers[1:4]) # Output: [20, 30, 40]

# # Slice from start to index 2
# print(numbers[:3]) # Output: [10, 20, 30] OR
# print(numbers[0::3])

# # Slice all alternate elements
# print(numbers[0:6:2]) # Output: [10, 30, 50,65] (start:stop:STEP)  OR
# print(numbers[::2])  # Output: [10, 30, 50,65,89] here only step is given so it run 1st to last

# # Slice with negative indices
# print(numbers[-4:-1]) # Output: [30, 40, 50]

# ## REVERSE LIST... *
# print(numbers[::-1]) # Output: [60,50,40,30,20,10] here only STEP is give -1 means run revrse(last to 1st)





### 4.. MODIFYING LIST ##  or[list method (search all in google or pdf)] or w3school
'''Lists are mutable, meaning you can change their content after creation. You can add,
remove, or change elements in a list.'''

# Initial list: 
# fruits2 = ["apple", "banana", "cherry" , "banana", "papaya",]

# # 1.. Changing an element
# fruits2[1] = "blueberry"
# print(fruits2)    # Output: ['apple', 'blueberry', 'cherry']


# #2.. Adding an element
# fruits2.append("mango")
# print(fruits2) # Output: ['apple', 'blueberry', 'cherry’, 'mango']

# fruits.append(456)
# print(fruits)   # Output: ['apple', 'blueberry', 'cherry’, 'mango', 456]


# 3..Removing an element
# fruits2.remove("cherry")
# print(fruits2) # Output: ['apple', 'blueberry', 'mango']
#     # if ther is same element two times the 'REMOVE' METHOD only remove 1st elemet/n
#    # because you know python used  interepeter  and so on......

# # 4..Extend 
# more_fruits = ['cherry','date']
# fruits2.extend(more_fruits)
# print(fruits2)


# 5..insert
# fruits2.insert(1,'chiku')  # here 1 is index number
# print(fruits)
# # 6..finding index
# index= fruits2.index('blueberry')
# print(index)

# # 7..find index - within a range
# index = fruits2.index('banana',2)
# print(index) #output 2

# # 8..count elements
# count = fruits2.count('banana')
# print(count)

# # 9..reverse list
# fruits2.reverse()
# print(fruits2)

# ## SORTING

# 10..sorting string in list 
# fruits2.sort() # DEFAULT char ascnding order
# print(fruits2)

# #  ... sorting with key length  ##
# fruits.sort(key=len) # min to max
# print(fruits)


# 12,sorting with key length
# fruits2.sort(key=len , reverse = True) # max to min
# print(fruits)

# # 13, sorting list {ascending order}
# num = [40,50,30,60,10,35]
# numbers.sort()      # defalut sort ascending order
# print(numbers)


# # 14, sorting list {descending order}
# num2 = [40,50,30,60,10,35]
# numbers.sort(reverse = True)      #sort descending order
# print(numbers)

# # 15, POP with index value
# popped = num.pop(2)
# print(popped)  # popped 2nd index value and print
# print(num)

# # 16, popped with default 
# last = num.pop()
# print(last)
# print(num)

# # 17, copying list
# copy_fruits = fruits2.copy()
# print(copy_fruits)

# # 18, copying list - modifying the copy not affect the original
# copy_fruits.append('grapes')
# print(copy_fruits)
                   

# # 19, clear
# fruits2.clear()
# print(fruits2) # output : [ ]




# ### 5 .. JOINING LIST  .. #
# '''
# There are several ways to join, or concatenate, two or more lists in Python.'''

# list1 = [1, 2]
# list2 = ["a", "b"]

# # 1. One of the easiest ways are by using the + operator
# list3 = list1 + list2
# print(list3) # Output: [1, 2, 'a', 'b']
 

# # 2. using append method

# for x in list2:
#     list1.append(x)
# # appending all the items from list2 into list1, one by one
# print(list1) # Output: [1, 2, 'a', 'b']


# #3. using extend method
# list1.extend(list2) # add elements from one list to another
# list
# print(list1) # Output: [1, 2, 'a', 'b']













##  .. ITRATTING OVER LIST    .. #

#Iterating allows you to traverse each element in a list, typically using loops.
#Example:
fruits = ["apple", "banana", "cherry"]
# Using for loop
for fal in fruits:
   print(fal)



# Using while loop
fruits_0 = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits_0):
    print(fruits_0[index])
    index += 1

#index += 1   (agar index me indentation na de to wo infinte loop me chal jaega)

#_______________________________________________________________________________________________________________________


# CHAPTER -- 11


## LIST COMPREHENSION
'''List comprehensions provide a concise way to create lists. They consist of brackets
containing an expression followed by a for clause, and optionally if clauses.
(OPTIMIZE tarika jis se ham list bana sakte hai)
NOTE - Syntax:
   new_list = [expression FOR item IN iterable IF condition] '''
# 3 main component of list comprehension
# -- 1. expression,  2. for clause,  3. if conditioin

# # create a list of square
# squares = [x**2 for x in range (1,6)]
# print(squares) #output-- [1, 4, 9, 16, 25]

# # Filter even number
# even_list = [x for x in range(1,20) if x%2 == 0 ]
# print(even_list)       #output--    [2, 4, 6, 8, 10, 12, 14, 16, 18]

## apply function to each element of list

# my_name = "aniket"
# print(my_name)     #output--  aniket
# print(my_name.upper())       #output-- ANIKET


my_list = ["apple", "orange", "cherry", "apple"]
# print(my_list.upper()) # this is wrong way  ERROR
# # .upper (object ) dees not work in list so

 #apply function to each element of list

# print(my_list[0].upper())   
# print(my_list[1].upper())   # converts each one isn't leghty process
# print(my_list[2].upper())    # and its oputput in multiple line
# print(my_list[3].upper())

# SO EITHER we use LIST COMPREHENSION (and its convert whole in 1st time and in 1 line )

# uppercase_list =[lst.upper() for lst in my_list]
# print(uppercase_list)     #output--  ['APPLE', 'ORANGE', 'CHERRY', 'APPLE']

# NOTE - we also read like this --    uppercase_list = lst
#                                      for lst in my_list:
#                                         lst.upper()
#                                         print(uppercase_list)




### 2...FLATTEN A NESTED LIST USING LIST COMPREHENSION

nested_list = [[1,2],[3,4],[5,6]]

# which means we have given nested list and we have to remove nested and convert into simple list

# # now 1st of all we do same basics
# for sublist in nested_list:  # is tarike se kuch aie print hoga
#    print(sublist)
# #output--   [1, 2]
#           [3, 4]
#           [5, 6]

# for sublist in nested_list:
#    print(nested_list)  # is tarike se kuch aie print hoga

# # output -- [[1, 2], [3, 4], [5, 6]]
#           [[1, 2], [3, 4], [5, 6]]
#           [[1, 2], [3, 4], [5, 6]] 


# for sublist in nested_list:  # is tarike se kuch aisa output hoga
#    for item in sublist:
#       print(item)
   
# output--
# 1
# 2
# 3
# 4
# 5
# 6

# and list comprehension s

# result = [item for sublist in nested_list for item in sublist]
# print(result) # ye ouput aaega

# output-- [1, 2, 3, 4, 5, 6]     aagya

#A. - for sublist in nested_list    | for item in sublist 
# first ,[1,2]-> and breakdown --   |    1,2
#  second,[3,4]-> and breakdown --  |    3,4
# third ,[5,6]-> and breakdown --   |    5,6
# and last me sabko merge kar diya



# OR now ham ise function me karte hai

# def flatten_list(lst):
#     return[item for sublist in lst for item in sublist]

# final_list = flatten_list(nested_list)
# print(final_list)

#OR 1 or TARIKA sir ek hi argument pe kam karega utna badhiya nhi hai
def flatten_list(nested_list):
    return[item for sublist in nested_list for item in sublist]

flatten_list(nested_list)
print(flatten_list(nested_list))


#____________________________________________________________________________________________________________________

#CHAPTER -- 12

### TUPLE ### -- (...) YE PARENTHESIS KE ANDAR HOTA HAI

'''
A tuple is a collection of items in Python that is ordered, unchangeable (immutable) and
allow duplicate values. it is simalr to list but not same
Tuples are used to store multiple items in a single variable.
NOTE: Ordered – Tuple items have a defined order, but that order will not change.
Example:'''

# fruits = ("apple", "orange", "cherry", "apple")
# print(fruits)

# # Output: ('apple', 'orange', 'cherry', 'apple')


## 1.. Creating a tuple

'''There are several ways to create a tuples in python :

1.. USING PARENTHESIS ( )
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = (1, [2, 3], (4, 5, 6))


2.. WITHOUT USING PARENTHESIS ( )
also_numbers = 1, 2, 3, 4, 5



3.. USING TUPLE ( ) CONSTRUCTOR 
new_tule = tuple(('apple','banana','cherry')) # using double ( )

list_items= ['x','y','z']   ## this is LIST 
tuple_items = tuple(list_items) # changing into tuple

#output -- ('x','y','z')




4. Single-Item Tuple
tuplesingle = ("only",) #  NOTE - here comma (,) is very important in last otherwise py consider it is STRING

'''



## 3..   Accessing Tuple Elements - Indexing  ##

'''You can access elements in a tuple by referring to their index. Python uses zero-based
indexing, meaning the first element has an index of 0.

NOTE- Syntax: tuple_name[index]

Example: 
'''
#INDEX =    0         1       2          3         4       # POSITIVE INDEX
fruits = ("apple", "orange", "cherry", "apple", "mango")
#            -5      -4          -3       -2     -1        # NEGATIVE INDEX

# # Access first element
# print(fruits[0]) # Output: apple

# # Access third element
# print(fruits[2]) # Output: cherry

# # Access last element using negative index
# print(fruits[-1]) # Output: mango



### 3. TUPLE SLICING  #
'''Slicing allows you to access a range of elements in a Tuple. You can specify the start and
stop indices, and Python returns a new tuple containing the specified elements.

NOTE -- Syntax: tuple_name[start:stop:step]'''  # start is include / but not stop(stop-1)
                                            # default start value is 0 and stop value is -1(last one) {index}
numbers = [10, 20, 30, 40, 50, 60 ,65,75,89]

# # Slice from index 1 to 3
# print(numbers[1:4]) # Output: [20, 30, 40]

# # Slice from start to index 2
# print(numbers[:3]) # Output: [10, 20, 30] OR
# print(numbers[0::3])

# # Slice all alternate elements
# print(numbers[0:6:2]) # Output: [10, 30, 50,65] (start:stop:STEP)  OR
# print(numbers[::2])  # Output: [10, 30, 50,65,89] here only step is given so it run 1st to last

# # Slice with negative indices
# print(numbers[-4:-1]) # Output: [30, 40, 50]

# ## REVERSE TUPLES... *
# print(numbers[::-1]) # Output: [60,50,40,30,20,10] here only STEP is give -1 means run revrse(last to 1st)


## 4.. TUPLE OPERATIONs ##

'''' 1. Concatenation
 You can join two or more tuples using the + operator.'''

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5)
# combined = tuple1 + tuple2
# print(combined) # Output: (1, 2, 3, 4, 5)




'''2. Repetition
# You can repeat a tuple multiple times using the * operator.'''

# tuple3 = ("hello",) * 3  # singel tuple with comma(,) remember
# print(tuple3) # Output: ('hello', 'hello', 'hello’)

# tuple4=(1,2,3,4)* 3
# print(tuple4) # output: (1,2,3,4,1,2,3,4,1,2,3,4)


'''3. Checking for an Item
# Use the in keyword to check if an item exists in a tuple.'''

# numbers = (10, 20, 30, 40)
# print(20 in numbers) # Output: True


## 5.. Iterating Over Tuple
'''Iterating allows you to traverse each element in a tuple, using loops.
examples:'''

fruits = ('apple','mango','pinapple')

#using for loop
# for fal in fruits:
#     print(fal)  # OR
#     print(fruits)  # dono me antar hai fal or fruits me
# #output --

# using while loop
# i = 0
# while i < len(fruits):
#     print(fruits[1])
#     i += 1



##..6  TUPLE METHODS #
#Python provides two built-in methods to use on tuples.

# count
# colors = ("red", "green", "blue", "green")
# print(colors.count('green')) # Output: 2



# # index
# colors = ("red", "green", "blue", "green")
# print(colors.index("green")) # Output: 1// 2nd green ko ignore karega





##.7.. TUPLE FUNCTION #

#Python provides several built-in functions to use on tuples.

# numbers= (9,5,3,2,6,7,5,3,1)

# #'len
# print(len(numbers))   #output- 9

# #sum
# print(sum(numbers))  #output- 41

# #min ,#max
# print(min(numbers))  #output- 1

# print(max(numbers))   #output- 9


# #sorted
# print(sorted(numbers))  #output- [1, 2, 3, 3, 5, 5, 6, 7, 9]
#                          # tuple is now list due to sort
# # if we  sorted number in tuple  then

# a = sorted(numbers)
# num_sort = tuple(a)  # now it's in tuple
# print(num_sort)  #output- (1, 2, 3, 3, 5, 5, 6, 7, 9)





##8.. PACKING AND UNPACKING TUPLE #

#a. Packing is the process of putting multiple values into a single tuple.

# a = "aniket"
# b = 21
# c = "Engineer"
# tuple_pack = a,b,c # Packing values into a tuple
# print(tuple_pack) #output-  ('aniket', 21, 'Engineer')


#b. Unpacking is extracting the values from a tuple into separate variables.

# name, age, proffesion = tuple_pack
# print("Name is ",name)
# print("Age is ",age)
# print("Proffesion is ",proffesion)

#NOTE- unpacked in orderd ways according to pack item
# and item or variable are same


## 9.. MODIFYING TUPLEs - Immutable
'''Once a tuple is created, you cannot modify its elements. This means you cannot add,
remove, or change items.'''

tuple_num = (10,23,45)
# tuple_num[0] = 100   # Error  hoga 
#print(tuple_num)


# How to modify tuple??
# 1st converts {Tuple into List} then modiffy and again change {List into Tuples}

list_numbers = list(tuple_num)
list_numbers[0] = 100
print(list_numbers)  # output - [100, 23, 45]

# now convert LIST into tuple
tuple_num1 = tuple(list_numbers)
print(tuple_num1)   # output --(100, 23, 45)


#NOTE - we can do all list/tuple methods by this technique
#eg like - append, remove , etc......



## 10.. Tuple Use Case - Examples

#Storing Fixed Data (Immutable Data)
'''Example: Storing geographic coordinates (latitude, longitude) or RGB color values, where
the values shouldn’t be changed after assignment.'''

coordinates = (40.7128, -74.0060) # Latitude and longitude for NYC
rgb_color = (255, 0, 0) # RGB value for red


## Using Tuples as Keys in Dictionaries
'''Since tuples are immutable and hashable, they can be used as keys in dictionaries, unlike
lists.'''
location_data = {
(40.7128, -74.0060): "New York City",
(34.0522, -118.2437): "Los Angeles"
}
print(location_data[(40.7128, -74.0060)]) # Output: New York City





#____________________________________________________________________________________________________________________

#CHAPTER -- 13

### `SETS` #  

# NOTE- sets in curly braces    { .. }

'''A set is a collection of unique items in Python. Sets do not allow duplicate items and do
not maintain any particular order so it can’t be indexed.

Characteristics of Sets:
• Unordered: Elements have no defined order. You cannot access elements by index.
• Unique Elements: No duplicates allowed. Each element must be distinct.
• Mutable: You can add or remove elements after creation.
• Immutable Elements: individual elements inside a set cannot be modified/replaced
NOTE- SETS is MUTABLE but SET Element isI IMUTABLE (we only add / remove but not REPLACE)
Example:'''
# vowels = {'a', 'e', 'i', 'o', 'u'}

# ## 1.. CREATING A SET #
# #There are two primary ways to create a set in Python:

# # 1. Using Curly Braces {}
# my_set = {1, 2, 3, 4, 5}
# print(my_set) # Output: {1, 2, 3, 4, 5}

# #2. Using the set() Constructor
# my_set = set([1, 2, 3, 4, 5])       # list convert into set
# print(my_set) # Output: {1, 2, 3, 4, 5}

# #NOTE-: An empty set cannot be created using {} as it creates an empty dictionary.
# #  Use set() instead.

# empty_set = set()
# print(empty_set) # Output: set()



##... 3. SET OPERATION .. ##


# #1. ADDING ELEMENT : USE the add() method to add a single element to a set.
# fruits = {'apple', 'banana'}
# fruits.add('cherry') 
# print(fruits)   # output-- {'banana', 'cherry', 'apple'}
# #NOTE-- cherry set me kisi v index me add ho jaega randomly qk set unodered hota hai



#2. 2. Removing Elements: Use the remove() or discard() methods to remove elements.
''' • remove() raises an error if the element is not found.
    • discard() does not raise an error if the element is missing.'''

# fal = {'banana', 'cherry', 'apple'}
# # using remove()
# fal.remove('banana')
# print(fal)    # output--  {'cherry', 'apple'}

# fal.remove('orange')   # error show karega
# print(fal)

# # using discard()
# fal.discard('banana')
# print(fal)      # output--  {'cherry', 'apple'}

# fal.discard('orange')  # discard error show nhi karega ye chill hai!
# print(fal)      # output--  {'cherry', 'apple'}


###.. SET METHOOD .. ##

# #1. UNION : Combines elements from two sets, removing duplicates.
# set1 = {1,2,3}
# set2 = {3,4,5}
# union_set = set1.union(set2)
# print(union_set)  # Output: {1, 2, 3, 4, 5}

# ##.UNION (alternative) |
# #Alternative Syntax: union_set = set_a | set_b
# union_set2= set1 | set
# print(union_set2)   # Output: {1, 2, 3, 4, 5}




# #2. INTERSECTON :Includes only elements present in both sets.(COMMON)
# setA = {1,2,3,4}
# setB = {2,3,4}
# intersection_set =setA.intersection(setB)
# print(intersection_set)  # Output: {2, 3}


# ## INTERSECTION (ALTERNATIVE)  &    
# #Alternative Syntax: intersection_set = set_a & set_b

# intersection_set1 =setA.intersection(setB)
# print(intersection_set1)  # Output: {2, 3}



# #3..DIFFERENCE : Elements present in the first set but not in the second.

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5}
# difference_set = set_a.difference(set_b)
# print(difference_set) # Output: {1, 2}

# # DIFFERENCE alternative -
# #Alternative Syntax: difference_set = set_a - set_b

# difference_set1 = set_a-set_b
# print(difference_set1) # Output: {1, 2}


# #4. SYMMETRIC DIFFERENCE: Elements in either set, but not in both.

# set_c = {1, 2, 3}
# set_d = {3, 4, 5}
# sym_diff_set = set_a.symmetric_difference(set_b)
# print(sym_diff_set) # Output: {1, 2, 4, 5}

# # ALTERNATIVE SYMMETRIC ^
# #Alternative Syntax: sym_diff_set = set_a ^ set_b

# sym_diff_set1 = set_a ^ set_b
# print(sym_diff_set1) # Output: {1, 2, 4, 5}



## .. SET ITRATION ..  ##
#You can use a for loop to go through each element in a set.


# Using FOR LOOP  - Printing each number from a set

numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(num)

# using WHILE LOOP -- don't support (1st convert into LIST then apply WHILE LOOp)



##.. SET COMPREHENSION .. ##

'''Set comprehensions allow concise and readable creation of sets. Similar to list
comprehensions but for sets.'''
#NOTE- SYNTAX: new_set = {expression FOR item IN itrable IF condition}


# Example:
squares = {x**2 for x in range(1, 6)}
print(squares) # Output: {1, 4, 9, 16, 25}



## .. SOME COMMON CASE ..##


'''
Set Common Use Cases:
• Removing Duplicates: Easily eliminate duplicate entries from data.
• Membership Testing: Quickly check if an item exists in a collection.
• Set Operations: Perform mathematical operations like union, intersection, and
difference.
• Data Analysis: Useful in scenarios requiring unique items, such as tags, categories,
or unique identifiers.'''


# Example: Removing Duplicates from a List
num = [1,2,3,4,4,5,5,6,6,7,7,8]
unique_numbers = set(num)
print(unique_numbers) # Output: {1, 2, 3, 4,}






#____________________________________________________________________________________________________________________

#CHAPTER -- 14

### ...  DICTIONARY  .. ###
'''
A dictionary is a data structure in Python that stores data in key-value pairs.
Dictionary items (key – value pair) are ordered, changeable, and do not allow duplicates.
• Key: Must be unique and immutable (strings, numbers, or tuples).
• Value: Can be any data type and does not need to be unique.'''

# #Example: Simple dictionary with three key-value pairs
# student2 = {1:"class - x",
#            "name" : "aniket",
#            "age" : 20
#            }
# print(student2)
# print(type(student))

## CREATE DICTIONARY IN PYTHON >>

'''Method-1: We create a dictionary using curly braces {} and separating keys and values
with a colon.
NOTE- Syntax:
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3", ...}'''


# Empty dictionary
empty_dict = {}


# Dictionary with data
cohort = {
            "course": "Python",
            "instructor": "Rishabh Mishra",
            "level": "Beginner"
}


'''Method-2: Using dict() constructor
Pass key-value pairs as keyword arguments to dict()'''
# PERSON = dict(name = 'madhav', age = 20, city = 'bhopal')
# print(PERSON)
# #OUTPUT -- {'name': 'madhav', 'age': 20, 'city': 'bhopal'}


'''Method-3: Using a List of Tuples
Pass a list of tuples, where each tuple contains a key-value pair.'''

# student1 = dict([('name','aniket'),('age', 20),('city ', 'bhopal')])
# print(student1)
#   #Output >>  {'name': 'aniket', 'age': 20, 'city ': 'bhopal'}



## 3.. ACCCESS DICTIONARY VALUES ..##
#Access dictionary values by using the key name inside square brackets.

# Example:

# student = {
# 1: "Class-X",
# "name": "Madhav",
# "age": 20
# }
# # print value based on respective key-names
# print(student["name"])  #Output >> Madhav
# print(student['age'])  #Output >> 20


# • .keys(): Returns all keys in the dictionary.
# • .values(): Returns all values in the dictionary.
# • .items(): Returns all key-value pairs.
# • .get(): Returns value for a key (with an optional default if key is missing).
# '''
# #Examples
# print(student.keys()) # All keys
# print(student.values()) # All values
# print(student.items()) # All key-value pairs
# print(student.get("name")) # Safe way to access a value




##.. 4 ADD, MODIFY & REMOVE ITEMS ..##

# student = {
# 1: "Class-X",
# "name": "Madhav",
# "age": 20
# }

# '''1. Add or Modify Item: Use assign-operator '=' to add/modify items in a dictionary.'''

# # Adding a new key-value pair
# student["email"] = "madhav@example.com"
# print(student)
# #OUTPUT --  {1: 'Class-X', 'name': 'Madhav', 'age': 20, 'email': 'madhav'

# # Modifying an existing value
# student["age"] = 25
# print(student)
# #OUTPUT -- {1: 'Class-X', 'name': 'Madhav', 'age': 25}

# '''2. Remove Item: Use del or .pop() to remove items from a dictionary.'''

# # Remove with del
# del student["age"]
# print(student)
# #OUTPUT --  {1: 'Class-X', 'name': 'Madhav', 'email': 'madhav@example.com'}

# # Remove with pop() and store the removed value
# email = student.pop('email')
# print(email)
# #OUTPUT --  madhav@example.com


## .. 5 . DICTIONARY ITRATION ..##

# student = {
# 1: "Class-X",
# "name": "Madhav",
# "age": 20
# }
# student["email"] = "madhav@example.com" # adding 1 key value

# # Loop through keys
# for key in student:
#     print(key)
# #OUTPUT --
# # 1
# # name
# # age
# # email


# oR 
# for X in student:
#     print(X)




# # Loop through values
# for value in student:
#     print(student[value])
# #OUTPUT --
# # Class-X
# # Madhav
# # 20
# # madhav@example.com




# # Loop through values: using values() method
# for value in student.values():
#     print(value)
# #OUTPUT --
# # Class-X
# # Madhav
# # 20
# # madhav@example.com


# # Loop through both keys and values
# for key, value in student.items():
#     print(key, value)
# #OUTPUT --
# # 1 Class-X
# # name Madhav
# # age 20
# # email madhav@example.com




## ..6.  NESTED DICTIONARY ..##

'''Dictionaries can contain other dictionaries, which is useful for storing more complex data.'''
#nested dictionary

main_student = {

    'student1' : {'name': "ANIKET","age":20 },
    'student2' : {'name' : "amarjeet", "age" : 22 , "grade" : 'A+' }
}
print(main_student)

# access value
print(main_student['student1']['name']) #output -- ANIKET
print(main_student['student2']['name']) #output -- amarjeet


##.. 7 . DICTIONARY COMPREHENSION ##
'''A dictionary comprehension allows you to create dictionaries in a concise way.'''

# Syntax:
#new_dict = {key_expression: value_expression for item in iterable if condition}

my_dict = {x:x+x for x in range (1,6)}
print(my_dict)

## DICTIONARY COMMON USE CASE>>##

'''• User Profiles in Web Applications: Store user details like name, email, etc.

• Product Inventory Management: Keep track of stock levels for products in an e-
commerce system.

• API Responses: Parse JSON data returned from APIs (e.g., weather data).
• Grouping Data: Organize data into categories. Example: grouped = {"fruits":
["apple", "banana"], "veggies": ["carrot"]}

• Caching: Store computed results to reuse and improve performance. Example:
cache = {"factorial_5": 120}

• Switch/Lookup Tables: Simulate switch-case for decision-making.
# Example:

actions = {"start": start_fn, "stop": stop_fn}
actions["start"]()'''
















#____________________________________________________________________________________________________________________

#CHAPTER -- 15


 ##.. OOPS ..##

#Q- CREATNG STUDENT RECORDS.. (using list )
# LIST
#STUDENT DETAILS

# student_1 =['Aniket', 10] # Name, grade
# student_2 =['Ammann', 8] # Name, grade
# print(student_1[0])
# print(student_1[1])
# print(f"{student_1[0]} is in class {student_1[1]}")
# print(f"{student_2[0]} is in class {student_2[1]} ")
# student_1.append('A')
# print(student_1)

## IN THIS pattern therr is lot of limitation
# SO WE USE { OOPs }

'''
Why OOPs?  
• Models Real-World Problems:  
 Mimics real-world entities for easier understanding. 
• Code Reusability:  
 Encourages reusable, modular, and organized code. 
• Easier Maintenance:  
 OOP organizes code into small, manageable parts (classes and objects). Changes in 
one part don’t impact others, making it easier to maintain. 
• Encapsulation:  
 Encapsulation protects data integrity and privacy by bundling data and methods 
within objects. 
• Flexibility & Scalability:  
 OOP makes it easier to add new features without affecting existing code. 
 
'''

## now  USING OOPs



# 1st. THiNG iS -- CLASS (blueprint or template) {in class method = function}

# 2nd. THiNG iS -- OBJECT (instance of class)       
# AGAIN CREATING STUDENT RECORD

# 1st. THiNG iS -- CLASS (blueprint or template) {in class method = function}
#2nd. THiNG iS -- OBJECT (instance of class)

##class
# class Student:
#     name = "aniket"
#     grade = 10


# #object
# student1 = Student()
# print(student1.name, student1.grade)

# #object - 2
# student2 = Student()
# print(student2.name, student2.grade)

# here both output is same because we hold the value is hard code value.,
# we cannot give any user input/ or any kind of Argument/ any parameter.


# then we Give argument (function == method in class)
# #         and we give it multiple argument like we add in percentage and many more 







# class Student:
#     def __init__(self, full_name, class_grade): # {init = initalise or init is name  and (it initalise object which we give) }
#                                             # and give parameter = (self) , it is compulsary when we use __init__
#             self.name =full_name   # Attribute
#             self.grade =class_grade   # Attribute
      
# #object 
# student1 = Student("aniket",12)
# ##student1 = Student("aniket",12 ,13) #(and if we give 1 extra parameter the it show error)
# print(student1.name, student1.grade)  #output--aniket 12


# #object -2
# student2 = Student("amarjeet", 11)
# print(student2.name, student2.grade)


# # here we can create multiple object with different values
# #object -3
# student3 = Student("Ammann", 8) 
# print(student3.name, student3.grade)  #output--Ammann 8

# print(student1.__dict__)
# print(student2.__dict__)







### in same class taking two method  ##

class Student:   # class
    def __init__(self,name,grade,percentage): # method (in braces- argument)
        self.name = name   # attributes
        self.grade= grade  # "  "
        self.percentage = percentage  # " "

    def student_details(self): #method
        print(f"{self.name} is in class {self.grade} and he got {self.percentage} % ")

#object 1
student1 = Student("madhav", 10 ,89)   # pass vlue in method 1


#object 2
student2 = Student("aniket", 12 , 60)  # pass vlue in method 1


print(student1.grade)
print(student1.name)
print(student1.name , student1.grade)

student1.student_details()   # pass vlue in method 2

print(" ")

print(student2.grade)
print(student2.name)
print(student2.name , student1.grade)

student2.student_details()  # pass vlue in method 2

print(student1.percentage)  # we add percentage (argument) later
print(student2.percentage)


#NOTE--> if we print whole value of student 1 OR student 2 just use __dict__ and see magic !!


print(student1.__dict__)
print(student2.__dict__)


### METHODS ##

## 1.. MODIFY OBJECT PROPERTY ##

print(student1.percentage)
student1.percentage = 100 #modify
print(student1.percentage)



## 2.. DELETE  OBJECT PROPERTY ##
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)


## 3.. DELETE OBJECT 
## del student1
# print(student1)





#___________________________________________________


# # in same class taking two method

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade= grade
#         self.percentage = percentage

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade} and he got {self.percentage} % ")

# #object 1
# student1 = Student("madhav", 10 ,89)


# #object 2
# student2 = Student("aniket", 12 , 60)


# print(student1.grade)
# print(student1.name)
# print(student1.name , student1.grade)
# student1.student_details()

# print(" ")

# print(student2.grade)
# print(student2.name)
# print(student2.name , student1.grade)
# student2.student_details()

# print(student1.percentage)  # we add percentage (argument) later
# print(student2.percentage)


# #NOTE--> if we print whole value of student 1 OR student 2 just use __dict__ and see magic !!


# print(student1.__dict__)
# print(student2.__dict__)











#____________________________________________________________________________________________________________________

#CHAPTER -- 16