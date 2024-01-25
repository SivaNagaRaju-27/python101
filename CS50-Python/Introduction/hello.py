x = "This is CS50P"
def main():
    name = input("Enter your name? ").strip().title()

    #String method to remove whitespaces
    '''name = name.strip().title()'''

    #Capitalize first letter of String.
    '''name = name.capitalize()
       name = name.title()
    '''

    #Splitting String into SubStrings.
    first, last = name.split(" ")

    #Partial syntax of print.
    print(f"Hello {first}", x, sep = "-", end = "__")

    #Formatted Printing
    print(f"I am Siva Naga Raju {x}")

main()
