def main():
    from matrix_base import get_random_matrix, print_matrix
    from matrix_arithmatic import matrix_multiplication
    n = int(input("How Many Matrices are There? "))
    orders = []
    for i in range(n):
        orders.append(input(f"What's Matrix{i+1} Order(eg: 2x3)? "))
    
    matrices = []
    for x in orders:
        if len(x) == 2:
            row_len = int(x[0])
            col_len = int(x[1])
            matrices.append(get_random_matrix(row_len, col_len))
        else:
            order = int(x[0])
            matrices.append(get_random_matrix(order))

    for mat in matrices:
        print_matrix(mat)
        print()
    
    product = matrices[0]
    i = 1
    while i < n:
        product = matrix_multiplication(product, matrices[i])
        i += 1

    print_matrix(product)

if __name__ == "__main__":
    main()