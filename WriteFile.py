# open external file for writing
users = open("2020members.txt", "w")
#add data to the external file
users.write("Dave")
users.write("\n")
users.write("Sarah")
users.write("\n")
users.write("PauLl")
users.write("\n")
#close the external file
users.close()