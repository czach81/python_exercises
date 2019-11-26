import sys
import random

ans = True

while ans:
    quesiton = input("Ask the Magic 8 ball a question (pre enter to quit) ")

    answers = random.randint(1, 8)

    if quesiton == "":
        sys.exit()

    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook is good")

    elif answers == 3:
        print("You may rely on it")    

    elif answers == 4:
        print("Never")

    elif answers == 5:
        print("Ask again later")

    elif answers == 6:
        print("I think you are on to something, but ask again")

    elif answers == 7:
        print("Not happening this year maybe next year")

    elif answers == 8:
        print("Better off sticking to your day job")
