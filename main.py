import os
import random
import json

usersList = []


def user_append():
    print('Enter your Desired Used ID: ')
    userId = input()
    print('Enter the amount of wheels between your Event Dates: ')
    count = input()
    i = 0
    while i < int(count):
        usersList.append(userId)
        i += 1

    do_you_wish()


def do_you_wish():
    print("Do you wish to proceed again? (Y / N) ")
    yes_or_no = input()
    if yes_or_no == "Y":
        user_append()
    else:
        print("Have a Nice Day!")


def winner_decider():
    return random.randint(0, len(usersList))


def json_create():
    jsonData = json.dumps(shuffledList)
    jsonFile = open("candidate_list.json", "w")
    jsonFile.write(jsonData)
    jsonFile.close()


babaSymbol = open("ascii-art.txt", "r")
print(babaSymbol.read())

print("Welcome to the Wheel of Wealth Special Event")
print("If you wish to proceed press Y then ENTER: ")
welcomeInput = input()

if welcomeInput == "Y":
    os.system('cls' if os.name == 'nt' else 'clear')
    user_append()
else:
    print("wut?")

shuffledList = random.sample(usersList, len(usersList))
print("The random number is : {0}".format(winner_decider()))
print("A json file has been generated for you comfort :)")
json_create()
print(shuffledList[winner_decider()])
print("Generated user is: {0}".format(shuffledList[winner_decider()]))
