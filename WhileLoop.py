letter = ""

while letter == "":
    letter = input("enter  ")
    if letter == "" :
        print ("no")

print("well done! Next game??")

while letter != "A" and letter != "B" and letter != "C" and letter != "D" and letter != "a" and letter != "b" and letter != "c":
    letter = input("enter  ")
    if letter != "A" and letter != "B" and letter != "C" and letter != "D" and letter != "a" and letter != "b" and letter != "c" :
        print ("no")

print("well done! Next game??")

while letter not in ("a","b","c"):
    letter = input("enter  ")
    if letter not in ("a","b","c"):
        print ("no !")

print("you won")