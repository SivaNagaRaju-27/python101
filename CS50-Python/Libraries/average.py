import statistics
mn = statistics.mean([100, 90])
print(mn)

def main():
    import sys
    try:
        print("Hello, My name is", sys.argv[1])
    except IndexError:
        print("Too few Arguments")
def main2():
    import sys
    if len(sys.argv) < 2:
        print("Too few arguments")
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        print("Hello, my name is", sys.argv[1])

def main3():
    import sys
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

main2()