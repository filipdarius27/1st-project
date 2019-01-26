import random
repeat = True
while repeat:
    response = input("Do you want to roll the dice? :3")
    if response == "Yes":
        print(random.randint(1, 6))
    elif response == "No":
        exit(0)
    else:
        print("You messed up! Only Yes/No answers are accepted!")
