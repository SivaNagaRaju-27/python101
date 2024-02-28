from matrix_base import is_not_matrix

def matrix_addition(m1, m2):
    if is_not_matrix(m1) and is_not_matrix(m2):
        print("These are Irregular Matrices...")
        return
    
    x1 = len(m1)
    y1 = len(m1[0])
    x2 = len(m2)
    y2 = len(m2[0])

    if (x1 != x2) and (y1 != y2):
        print("These Matrices are Not compatible for Addition...")
        return
    
    m = []
    r = 0
    for x in m1:
        c = 0
        m.append([])
        for i in x:
            m[r].append(i + m2[r][c])
            c += 1
        r += 1
    
    return m

def matrix_multiplication(m1, m2):
    if is_not_matrix(m1) and is_not_matrix(m2):
        print("These are Irregular Matrices...")
        return
    
    if len(m1) != len(m2[0]):
        print("These Matrices are Not Compatible for Multiplication...")
        return
    
    m = []
    i = 0

    while i < len(m1):
        m.append([])
        j = 0
        while j < len(m2[0]):
            k = 0
            sum = 0
            while k < len(m2):
                sum += m1[i][k] * m2[k][j]
                k += 1
            m[i].append(sum)
            j += 1
        i += 1
    
    return m

def matrix_subtraction(m1, m2):
    if is_not_matrix(m1) and is_not_matrix(m2):
        print("These are Irregular Matrices...")
        return
    
    x1 = len(m1)
    y1 = len(m1[0])
    x2 = len(m2)
    y2 = len(m2[0])

    if (x1 != x2) and (y1 != y2):
        print("These Matrices are Not compatible for Subtraction...")
        return
    
    m = []
    r = 0
    for x in m1:
        c = 0
        m.append([])
        for i in x:
            m[r].append(i - m2[r][c])
            c += 1
        r += 1
    
    return m


