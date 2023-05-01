#Create an algorithm using a loop to print out all the items of an array one at a time

cars = ['Ford', 'BMW', 'Renault', 'Jaguar', 'Peugeot', 'Vauxhall', 'Nissan']

for index in range(len(cars)):
  print(cars[index])
  index = index + 1

# note range(0,len(cars)) would also work
