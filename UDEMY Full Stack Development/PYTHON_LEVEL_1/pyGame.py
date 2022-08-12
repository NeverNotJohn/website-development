
from random import *

print("*** WELCOME TO CODEBREAKER *** \nTry to guess my 3 digit number bitch")

first_digit = 1
second_digit = 1
third_digit= 1

while(first_digit == second_digit or first_digit == third_digit or second_digit == third_digit):
    answer = str(randint(100, 999))
    first_digit = int(answer[0])
    second_digit = int(answer[1])
    third_digit = int(answer[2])

while (True):
    userInput = input("Insert 3 digit number: ")

    found = False

    if (userInput == answer):
        print("*** 🎊 WOOT YOU WON 🎊 ***")
        break

    for i in answer:
        for z in userInput:
            if (i == z):
                found = True
                if (answer.index(i) == userInput.index(z)):
                    print("Match! DUMMASSSSS")
                else:
                    print("Close")
                break
        if (found == True):
            break

    if (found == False):
        print("not even close bud")
