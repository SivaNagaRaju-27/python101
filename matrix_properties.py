from matrix_base import is_square_matrix

def sub_matrix(m, row, col):
    if not(is_square_matrix):
        print("This Matrix is Not a Square Matrix")
        return
    
    i = 0
    r = 0

    x = []

    while i < len(m):
        if i == row:
            i += 1
            continue

        x.append([])
        j = 0

        while j < len(m[0]):
            if j == col:
                j += 1
                continue

            x[r].append(m[i][j])
            j += 1

        i += 1
        r += 1
    
    return x
