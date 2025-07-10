# Function
"""
# A function is a block of reusable code that performs a specific task

def sum(a, b):  # 'sum' ek function hai jo do arguments (a, b) leta hai
    return a + b  # 'return' statement a + b ka result wapas deta hai jahan function call hua hai

# Function ko call karke uska result variable 'a' mein store kiya
a = sum(4, 8)  # yahaan 4 aur 8 values(arguments) diye gaye a aur b ko
print(a)  # print karega 12 (4 + 8 ka result)

# Yahaan function direct call hua hai bina kisi variable mein store kiye
print(sum(7, 8))  # ye direct 15 print karega
"""


#Global Variable and Local variable
"""
x = 101 # global Variable - variable which is stores outside the function

def func(x):
    x = 102 #local variable - variable which is stored inside the function
    print(x)

print(x) # ye global varuable print krega - output 101
func(x) # ye local variable print krega - output 102

#Or

x = 101 # global Variable - variable which is stores outside the function

def func(x):
    global x          # ye local variable ko global se replace kr dega
    x = 102           #local variable - variable which is stored inside the function
    print(x)

print(x) # ye global varuable print krega - output 101
func(x) # ye local variable print krega - output 102
print(x) # iss ka output 102 hoga global x use krne k kaaran 
"""


# Default argument
"""
def greet(name, message = 'Good morning'):
    print(name,message)

greet("Deepak") # default argument - ye output m good morning add kr dega 
greet("Hemlata", "Good Afternoon") # - ye output m good afternoon show krega
"""


#keyword argument
"""
def key_wordargument(name,age,gender):
    print(name,age,gender)

key_wordargument(name = "Deepak",gender = "Male",age = 23 ) #keyword aurgament - iss me position change kr skte hai
key_wordargument("Hemlata",25,"Female")  #positional argument - iss m sara position same hona chaiye
"""


# *args  (all arguments) -- list, tuple
"""
# They are used in function definitions to pass a variable number of arguments

def add_nums(*args):
    print(args)    #ye args ko pass kiye usko print kiya
    print("Sum = ",sum(args))

add_nums(5,6,8)  # non-keyworded variable-length arguments (like a list/tuple) - argument pass kiya

#or 

def names_args(*names):  
    for name in args:
        print(i)
        
names = ["Deepak","Hemlata","Girish","Rahul"]
names_args(*names)

"""


# **kwargs (all all key value arguments) -- dict
"""
def print_details(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():  
        print(f"{key}:{value}")

print_details(name= "Deepak", age = 25,gender = "Male")
"""

"""
def demo_func(a,b,*args,**kwargs):  # starting m normal arguments, uske baad *args , sabse last m **kwargs
    print(a)   
    print(b)
    print("args = ",args)
    print("kwargs = ",kwargs)

demo_func(1,2,4,5,6,7,name = "Deepak",age = 25,gender = "Male")
"""


# Lambda function
"""
# A lambda function is a small, anonymous function in Python used for quick, one-line operations
# Yeh anonymous function hai (iska koi naam nahi hota), isliye hum ise ek variable (jaise 'sum') mein store karte hain
# lambda x, y, z: x + y + z  --> yeh iska syntax hai:
# lambda       --> keyword
# x, y, z      --> parameters (arguments)
# x + y + z    --> expression (jo return karega)

sum = lambda x, y, z: x + y + z  # Lambda function ko 'sum' naam ke variable mein store kiya gaya hai

# Function call karke result print karte hain
print(sum(1, 3, 5))  # Output: 9

"""



# Class
"""
# A class is a blueprint for creating objects. It allows us to group data (attributes) and functions (methods) into a single structure.

#Example code

class Person:  # Ye ek class hai jiska naam hai 'Person'

    def __init__(self, name, age):  # Ye constructor hai, jo tab chalti hai jab object banate hain
        self.name = name  # 'self' ka matlab hai current object. 'name' ko uss object mein store kar rahe hain
        self.age = age  # 'age' bhi current object ke andar store ho raha hai

    def greet(self):  # Ye ek method hai (function jo class ke andar hota hai)
        print(f"Hello my name is {self.name} and my age is {self.age} years old")


# Yahan hum 'Person' class ka ek object bana rahe hain
person1 = Person("Deepak", 25)

# Object ke through class ka method call kar rahe hain
person1.greet()
"""


#Method and its Types
# A method is a function inside a class that works with the object of that class.
# 3 Types of Method are there 1-Instance Method,2-Class Method and 3- Static method


#1 Static Method
"""
# When you want to perform a specific action for an object, you use 'self' to define an instance method.
# Each object can have different values.

class Student:
    def __init__(self, name):  # This is an instance method (because it uses 'self')
        self.name = name

    def say_hello(self):  # Instance method
        print(f"Hello, my name is {self.name}")
"""


#2 Class Method
"""
# When you want to show or work with the same data for all objects (like school name),
# you use a class method with 'cls' to access class-level data.

class Student:
    school = "ABC School"  # Class variable

    @classmethod
    def show_school(cls):  # Class method (uses 'cls' instead of 'self')
        print(f"School Name: {cls.school}")

"""


#3 Static method
"""
# When your method does not depend on class-level or object-level data,
# and is just performing a general task or showing a message, use a static method.

class Student:
    @staticmethod  # Static method decorator
    def greet():  # Static method
        print("Welcome to the class!")
"""


#Constructor
"""
#A constructor is a special method that runs automatically when you create an object of a class.

class Person:
    def __init__(self, name):  # Constructor - self is an instance of that class
        self.name = name
        print(f"Object created for {self.name}")

p1 = Person("Deepak")  # Constructor is called automatically

#When you create an object, the __init__ method is triggered automatically. It’s used to initialize object attributes (like name, age, etc.).
"""


# Decorator
"""
# A decorator is a function that modifies or enhances another function without changing its code.
def my_decorator(func):  #ye hum ne decorator bnaya aur ye function lega
    def wrapper():            # ye wo wrapper function hai jo extra feature add krega
        print("Function is Starting")   # ye print hoga decorator k kaaran
        func() # ye hai humara original function
        print("Function has Ended") # ye print hoga decorator k kaaran
    return wrapper    # return kr denge hum toh ye extra feature se replace ke dega

@my_decorator   # Ye hum ne decorate kr diya aapne existing function ko
def say_hello():  # ye huma existing function
    print("Hello Deepak Yadav")   

say_hello()
"""


#generator
"""
# A generator is a function that returns values one at a time using the yield keyword, instead of returning them all at once

def my_generator():    # ye ek function bnaya hai
    for i in range(1,11):
        yield i         # jb hum return ki jagah yield use krenge toh vo generatior bn jyga

gen = my_generator()   iss function ko variavle m store kiya h

#print(next(gen))  # ye one return krega (step by step)
#print(next(gen)) #ye two return krega (next step)


for j in gen:  # ye hum ne for loop chala diya variable pe to print all elements (hr baar next thodi krenge)
    print(j)
"""


# OOPS Concept



