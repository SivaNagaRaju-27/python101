name = input("What's you name? ")

def assign(name):
    if name == "Siva":
        print("Gryfindor")
    elif name == "Phani":
        print("Gryfindor")
    elif name == "Raju":
        print("Gryfindor")
    elif name == "Bala":
        print("Slytherien")
    else:
        print("Who?")

def assign2(name):
    match name:
        case "Siva" | "Phani" | "Raju":
            print("Gryfindor")
        case "Bala":
            print("Slytherien")
        case _:
            print("Who?")

assign(name)
assign2(name)
