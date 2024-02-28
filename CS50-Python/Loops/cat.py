def sound1(s):
    print(s)
    print(s)
    print(s)

def sound2(s):
    i = 3
    while i != 0:
        print(s)
        i = i-1

def sound3(s,n):
    i = 0
    while i < n:
        print(i,s)
        i += 1

def sound4(s):
    for _ in [1,2,3]:
        print(s)

def sound5(s,n):
    for i in range(n):
        print(i, s)

s = input("Enter sound: ")
n = int(input("How many times we should print? "))
# sound3(s,n)
print((s+"\n")*n, end="")

# sound4("Mew")
