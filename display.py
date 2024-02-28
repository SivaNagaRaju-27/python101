def matrix(mat, name):
    r = len(mat)
    if r == 0:
        print("\t***----***")
        print("\t   |NA|")
        return

    clen = []
    i = 0

    while i < len(mat[0]):
        j = 0
        max_len = 0
        while j < len(mat):
            max_len = max(max_len, len(str(mat[j][i])))
            j += 1
        clen.append(max_len)
        i += 1
    
    rlen = sum(clen)

    q = len(name)
    c = len(mat[0])
    l = rlen + c - 1

    if l < 9+q:
        print("\t****-", end = "")
        i = 0
        while i < l:
            print("-", end = "")
            i += 1
        print("-****")
    else:
        if ((l%2 != 0) and (q%2 == 0)) or ((l%2 == 0) and (q%2 != 0)):
            temp = (9+q)/2
        else:
            temp = (8+q)/2
        
        print("\t*****", end = "")
        i = 0
        while i < (l/2 - temp - 1):
            print("*", end = "")
            i += 1
        print("|", end = "")
        print("Matrix", end = "")

        if ((l%2 != 0) and (q%2 == 0)) or ((l%2 == 0) and (q%2 != 0)):
            print("-",end = "")
        
        print(f"[{name}]", end = "|")

        i = 0
        while i < (l/2 - temp - 1):
            print("*", end = "")
            i += 1
        
        print("*****")
    
    for row in mat:
        print("\t    |", end = "")
        n = 0
        for item in row:
            if len(str(item)) < clen[n]:
                i = len(str(item))
                while i < clen[n]:
                    print(" ", end = "")
                    i += 1
                print(item, end = " ")
            else:
                print(item, end = " ")
            n += 1
        print("\b|")
