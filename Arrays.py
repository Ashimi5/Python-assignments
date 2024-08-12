#Creating an array

cars = ["Ford", "Volvo", "BMW"] 

#Accessing elements of array

x = cars[0] 

print(x)

#Modify the value of first array item 

cars[0] = "Toyota"

#Length of an array

x = len(cars) 


#Looping array elements

for x in cars:
  print(x) 


#Appending array elements

cars.append("Honda")


#Removing array elements

cars.pop(1) 

#Remove element that has value Volvo

cars.remove("Volvo") 


