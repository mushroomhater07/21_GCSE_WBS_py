# Declare a static array called cars with a length of 5 items
# Ask use to input the make of 5 types of car
# Print out the array

cars = [1,2,3,4,5] #unable to define length of a static array in python 
for index in range(5):
  cars[index] = input("Please enter the make of a car ")

print(cars)
