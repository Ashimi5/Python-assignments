# Classes and Objects

""""
class MyClass:              #Creating class
x = 5

p1 = MyClass()              #Creating object p1
print(p1.x)                 #Accessing elements of MyClass

"""

# Using init function

'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Ashim", 27)


print(p1.name)
print(p1.age) 

print(p2.name)
print(p2.age)
'''

#Using the str function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)





