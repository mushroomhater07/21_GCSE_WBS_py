nu8= -1
nu7= -1
nu6= -1
nu5= -1
nu4= -1
nu3= -1
nu2= -1
nu1= -1
number = input("Account")
nu1 = number[0]*8
nu2 = number[1]*7
nu3 = number[2]*6
nu4 = number[3]*5
nu5 = number[4]*4
nu6 = number[5]*3
nu7 = number[6]*2
nu8 = number[7]
check = nu1 + nu2 + nu3 + nu4 + nu5 + nu6 + nu7

digit = check % 11

check2 = 11 - digit
print(check2)

if check2 != nu8:
    print("sorry")
else:
    print("okay")