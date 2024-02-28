def choice1():
    import random
    n = int(input("Enter a Number: "))
    for i in range(n):
        x = random.choice(["Head", "Tails"])
        print(x)
    
def choice2():
    from random import choice
    n = int(input("Enter a Number: "))
    for i in range(n):
        x = choice(["Head", "Tails"])
        print(x)

def randomInt():
    import random

    number = random.randint(1, 10)
    print(number)

def shuffleList():
    import random
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for i in cards:
        print(i)


shuffleList()