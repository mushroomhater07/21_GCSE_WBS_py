from random import randint
from time import sleep
score = 0
numcheck = 0
def roll():
    print("Roll the dice")
    num3 = 0
    sleep(1)
    num1 = randint(1, 6)
    print("first number: " + str(num1))
    sleep(1)
    num2 = randint(1, 6)
    print("second number: " + str(num2))
    sleep(1)
    if num1 == num2:
        print("====one extra dice====")
        num3 = randint(1, 6)
        print("third number: " + str(num3))
    score = num1 + num2 + num3
    print("total: " + str(score))
    sleep(1)
    numcheck = score % 2
    if numcheck == 0:
        print("Yeah! even number! score +10")
        score = score + 10
    else:
        print("Ouch! odd number! score -5")
        score = score - 5
    sleep(1)
    return score
pruser1 = ""
pruser1pass = ""
pruser2 = ""
pruser2pass = ""
print("============Hello user1============")
turn = str(input("type anything and enter to continue: "))
user1 = str(input("create user1 username: "))
while len(user1) == 0:
    print("==input a valid username==")
    user1 = str(input("create user1 username: "))
user1pass = str(input("create user1 password: "))
while len(user1pass) <= 3:
    print("==input more than 3 character password==")
    user1pass = str(input("create user1 password: "))
print("============Hello user2============")
turn = str(input("type anything and enter to continue: "))
user2 = str(input("create user2 username: "))
while len(user2) == 0 or user1 == user2:
    print("==input a valid username==")
    user2 = str(input("create user2 username: "))
user2pass = str(input("create user2 password: "))
while len(user2pass) <= 3:
    print("==input more than 3 character password==")
    user2pass = str(input("create user2 password: "))
user1score = int(0)
user2score = int(0)
gamecount = int(0)
print("===there are 5 rounds of rolling dice===")
while gamecount != 5:
    print("============pass to user1============")
    turn = str(input("type anything and enter to start: "))
    pruser1 = str(input("input user1 username: "))
    while pruser1 != user1:
        print("==who are you?==")
        pruser1 = str(input("input user1 username: "))
    pruser1pass = str(input("input user1 password: "))
    while pruser1pass != user1pass:
        print("==Unauthorise==")
        pruser1pass = str(input("input user1 password: "))
    count = roll()
    print("your last score: " + str(user1score))
    user1score = user1score + count
    if user1score < 0:
        user1score = 0
        print("restored your score to 0")
    print("user1 score: " + str(user1score))
    print("============pass to user2============")
    turn = str(input("type anything and enter to start: "))
    pruser2 = str(input("input user2 username: "))
    while pruser2 != user2:
        print("==who are you?==")
        pruser2 = str(input("input user2 username: "))
    pruser2pass = str(input("input user2 password: "))
    while pruser2pass != user2pass:
        print("==Unauthorise==")
        pruser2pass = str(input("input user2 password: "))
    count = roll()
    print("your last score: " + str(user2score))
    user2score = user2score + count
    if user2score < 0:
        user2score = 0
        print("restored your score to 0")
    print("user2 score: " + str(user2score))
    gamecount = gamecount + 1
while user1score == user2score:
    print("========Deuce! one more turn========")
    print("============pass to user1============")
    turn = str(input("type anything and enter to start: "))
    pruser1 = str(input("input user1 username: "))
    while pruser1 != user1:
        print("==who are you?==")
        pruser1 = str(input("input user1 username: "))
    pruser1pass = str(input("input user1 password: "))
    while pruser1pass != user1pass:
        print("==Unauthorise==")
        pruser1pass = str(input("input user1 password: "))
    count = roll()
    print("your last score: " + str(user1score))
    user1score = user1score + count
    if user1score < 0:
        user1score = 0
        print("restored your score to 0")
    print("user1 score: " + str(user1score))
    print("============pass to user2============")
    turn = str(input("type anything and enter to start: "))
    pruser2 = str(input("input user2 username: "))
    while pruser2 != user2:
        print("==who are you?==")
        pruser2 = str(input("input user2 username: "))
    pruser2pass = str(input("input user2 password: "))
    while pruser2pass != user2pass:
        print("==Unauthorise==")
        pruser2pass = str(input("input user2 password: "))
    count = roll()
    print("your last score: " + str(user2score))
    user2score = user2score + count
    if user2score < 0:
        user2score = 0
        print("restored your score to 0")
    print("user2 score: " + str(user2score))
    gamecount = gamecount + 1
sleep(2)
print("====================finish!=====================")
turn = str(input("type anything and enter to continue: "))
sleep(1)
print("user1 score: " + str(user1score) + " | user2 score: " + str(user2score))
users = open("diceroll.txt", "a")
if user1score > user2score:
    print(user1 + " wins! User1 score " + str(user1score) + " marks!")
    users.write(str(user1score) + "     " + str(user1))
    users.write("\n")
    users.close()
else:
    print(user2 + " wins! User2 score " + str(user2score) + " marks !")
    users.write(str(user2score) + "     " + str(user2))
    users.write("\n")
    users.close()
sleep(2)
print("")
print("[score] [previous winner]:")
users = open("diceroll.txt", "r")
print(users.readline())
print(users.readline())
print(users.readline())
print(users.readline())
print(users.readline())
users.close()
#import json
#dict = {}
#with open("test.json", "r") as config_file:
#    dict = json.load(config_file)
print("====================done!=====================")