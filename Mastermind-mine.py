from random import randint

n1 = str(randint (1,9))
n2 = str(randint (1,9))
n3 = str(randint (1,9))
n4 = str(randint (1,9))
print(n1,n2,n3,n4)
trials = 5
while trials != 0:
    trials=0
    guess1 = str (input("guess 1st number"))
    while len(guess1) !=1 or guess1.isnumeric()==False:
        print("Not a correct number")
        guess1 = str (input("guess the 1st number"))
    guess2 = str (input("guess 2nd number"))
    while len(guess2) !=1 or guess2.isnumeric()==False:
        print("Not a correct number")
        guess2 = str (input("guess the 2nd number"))
    guess3 = str (input("guess 3rd number"))
    while len(guess3) !=1 or guess3.isnumeric()==False:
        print("Not a correct number")
        guess3 = str (input("guess the 3rd number"))
    guess4 = str (input("guess 4th number"))
    while len(guess4) !=1 or guess4.isnumeric()==False:
        print("Not a correct number")
        guess4 = str (input("guess the 4th number"))
    if guess1 != n1:
        trials +=1
    if guess2 != n2:
        trials +=1
    if guess3 != n3:
        trials +=1
    if guess4 != n4:
        trials +=1
    trial = 4-trials
    print(trial,"number at right pos")
print ("Well done")
def checknum():
    return()