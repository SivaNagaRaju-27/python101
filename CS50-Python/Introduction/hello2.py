def hello(to = "World"):
    print("Hello," ,to)

def main():
    hello()
    name = input("What's your name? ")
    hello(name)

main()
