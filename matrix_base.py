def get_random_matrix(row_len, col_len = -1):
    import random
    if col_len == -1:
        col_len = row_len
    
    i = 0
    m = []

    while i < row_len:
        m.append([])
        j = 0
        while j < col_len:
            m[i].append(random.randint(0, 1000))
            j += 1
        i += 1
    
    return m

def get_matrix(row_len, col_len = -1):
    if col_len == -1:
        col_len = row_len
    
    i = 0
    m =[]

    while i < row_len:
        m.append([])
        j = 0
        while j < col_len:
            m[i].append(int(input(f"Enter Ele-[{i+1}][{j+1}]: ")))
            j += 1
        i += 1
    
    return m

def print_matrix(m):
    for x in m:
        for i in x:
            print(i, end = " ")
        print("\b")

def is_not_matrix(m):
    lenth = len(m[0])
    for x in m: 
        if len(x) != lenth:
            return True
    
    return False

def is_square_matrix(m):
    if is_not_matrix(m):
        print("It's an Irregular Matrix")
        return False
    
    if len(m) != len(m[0]):
        return False
    
    return True
