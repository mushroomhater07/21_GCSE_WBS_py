def login():
    users = [["user1","password1"], ["user2","password2"], ["user3","password3"]]
    userEntry = ""
    foundName = 0
    correctPassword = False

    while userEntry == "" and correctPassword == False:
        userEntry = input("Please enter your username.\n")
        for index in range(0,len(users)):
            if userEntry == users[index][0]:
                foundName = 1
                attempts = 0
                while attempts < 3 and correctPassword == False:
                    passwordEntry = input("Please enter your password.\n")
                    if passwordEntry == users[index][1]:
                        print("Username and password are correct. ")
                        correctPassword = True
                    else:
                        print("Sorry, the password is incorrect. ")
                        userEntry = ""
                if attempts >= 3:
                    print ("Account has been locked...")
        if foundName == 0:
            print ("User name not recognised")
    return userEntry

print("Player1 login please\n")
player1 = "Tom" #login()
print("\nPlayer2 login please\n")
player2 = login()

print(player1,player2)
