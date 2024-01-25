x = int(input("What's x? "))
y = int(input("What's y? "))

def compr1(x, y):
    if(x < y):
        print("x is less than y")
    if(x > y):
        print("x is greater than y")
    if x == y:
        print("x is equal to y")

def compr2(x, y):
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

def compr3(x, y):
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

def compr4(x, y):
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

compr1(x,y)
compr2(x,y)
compr3(x,y)
compr4(x,y)
