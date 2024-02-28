def main():
    x = int(input("What's x? "))
    y = range(x)
    print(y)
    for i in y:
        print(i,"Hello World", sep = ": ")
    
main()