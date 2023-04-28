First = ""
Sur = ""
age = -1
letter = ("What house are u  ")
Pass = ("")
print("Here is your account Validation test---")
while First == "":
    First = input("Firstname  ")
    if First == "" :
        print ("again")
print ("Let me write that down 0_0 ")
while Sur == "":
    Sur = input("Surname  ")
    if Sur == "" :
        print ("again")
print ("Got it! Next question :)")
while letter != "Bereton" and letter != "Courtenay" and letter != "Fortescue" and letter != "Grenville" :
    letter = input("enter House  ")
    if letter != "Bereton" and letter != "Courtenay" and letter != "Fortescue" and letter != "Grenville":
        print ("again")
print ("Oh! same as mine :p")
while age > 120 or age <0:
    age = int(input("enter age  "))
    if age > 120 or age <0:
        print ("again")
print ("Nice to meet you @@")
while len(Pass) <8:
    Pass = input ("Password  ")
    if len(Pass) <8:
        print ("again")
print("OWO, I cant see it")
print("")
print("")
print("")
print("")
print("You are",First, Sur)
print(age, " years old.")
print("Password is " , Pass)
print("House is ", letter)
print("")