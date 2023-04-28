# open external file for writing
users = open("2020members.txt", "a")

# append data to the external file
name = input("enter")
users.write(name+"\n")

# close the external file
users.close()