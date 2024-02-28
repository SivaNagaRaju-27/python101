def readRandomList():
    import random
    n = int(input("What's the List size? "))
    i = 0
    list = []
    while i<n:
        list.append(random.randint(1, 100))
        i = i+1
    return list

def readList():
    n = int(input("What's the List size? "))
    i = 0
    list = []
    while i<n:
        list.append(int(input(f"What's Ele[{i+1}]? ")))
        i = i+1
    return list

def showList(list, msg="List"):
    print(f"\n{msg} =[", end = "")
    for i in list:
        print(i, end = ", ")
    print("\b\b]")

def sortCheck(list):
    n = len(list)
    i = 0
    while i < n-1:
        if list[i] > list[i+1]:
            return False
        i += 1
    return True