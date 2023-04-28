# Mastermind
import random

#Generate the random 4 digit target number
def random4digit():
    ran1 = str(random.randint(0,9))
#     randint is used for generate  number which is integer
    ran2 = str(random.randint(0,9))
    ran3 = str(random.randint(0,9))
    ran4 = str(random.randint(0,9))
    ranNum = ran1+ran2+ran3+ran4
    return (ranNum)

# Get userNumber
def getNumber():
    userGuess = str(input("Please input a 4 digit number "))
    #validation needed a) is it 4 digits b) are the digits 0-9
    #use of .isnumeric() found at w3schools.com
    if len(userGuess) != 4 or userGuess.isnumeric()==False:
        print ("Not a 4 digit number, please enter again ")
        userGuess = getNumber()
    return(userGuess)

#the main program
def main():
    target = random4digit()
    print(target) #output target for testing purposes
    #incorret guess so while loop runs at least once
    newGuess = "12345"
    counter = 1

    #repeat until correct number is found
    while target != newGuess:
        newGuess = getNumber()
        counter+=1
        correct = 0
        for index in range(4):
            if newGuess[index] == target[0] or newGuess[index] == target[1] or newGuess[index] == target[2] or newGuess[index] == target[3]:
                correct+=1
        print ("You have",correct,"numbers correct")
    print ("Congratulations your have found the correct number =>",target,"Guesstimes",counter,"-1")

main()