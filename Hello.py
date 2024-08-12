# Function without arguements
print("Function without arguements")

def my_function():
    print("Hello")

my_function()

#===============================================#

#Function with arguements
print("Function with arguements")

def my_function(fname):   #fname is arguement
    print(fname+"Sharma")

my_function("Hari")
my_function("Ram")


#===============================================#


#Function with multiple arguements
print("Function with multiple arguements")

def my_function(fname,lname):
    print(fname+""+lname)
my_function("Ram","Sharma")


#===============================================#

#Function with arbitrary arguements
print("Function with arbitrary arguements")

def my_function(*kids):
    print("The youngest child is " +kids[0])

my_function("Ashim","Bhagesh","Asmita")


#===============================================#


#Function with keyword arguements
print("Function with keyword arguements")

def my_function(child3,child2,child1):
    print("The youngest child is " +child1)

my_function(child1="Ashim",child2="Bhagesh",child3="Asmita")


#===============================================#


#Function with Arbitrary keyword arguements
print("Function with arbitrary keyword arguements")

def my_function(**kid):
    print("His last name is " +kid["lname"])

my_function(fname="Ashim",lname="Pandey")


#===============================================#


#Default parameter value
print("Function with default parameter value")

def my_function(country="Nepal"):
    print("I am from"+country)

my_function("India")
my_function("China")



#===============================================#


#Passing list as an arguement
print("Passing list as an arguement")

def my_func(food):
    for x in food:
        print(x)


fruits=["apple","cherry","banana"]

my_func(fruits)



#===============================================#

#Return values
print("Return Values")

def my_func(x):
    return 5*x

print(my_func(3))
print(my_func(5))




#===============================================#

#Pass statement for empty function
print("Pass statement")


def my_func():
    pass

#===============================================#

#Positional only arguements
print("Positional only arguements")

def my_function(x, /):
  print(x)

my_function(3) 

# OR

def my_function(x):
  print(x)

my_function(x = 3) 


#Lambda functions 
print("Lambda")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))