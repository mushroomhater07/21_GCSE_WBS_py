# open external file for writing
users = open("2020members.txt", "r")

# read data to the external file
print(users.read())
print("")
print(users.readline())
print(users.readline())

# close the external file
users.close()