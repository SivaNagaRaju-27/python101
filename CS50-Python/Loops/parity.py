def main():
    x = int(input("what's x?: "))
    print("The Number", x , "is "+evenORodd(x))

    if is_even3(x):
        print("Even")
    else:
        print("Odd")

def evenORodd(x):
    if(x%2 == 0):
        return "even"
    return "odd"

def is_even(n):
    if n%2 == 0:
        return True
    return False

def is_even2(n):
    return True if n%2 == 0 else False

def is_even3(n):
    return n%2 == 0

main()
