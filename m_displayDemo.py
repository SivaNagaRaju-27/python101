from display import matrix
from matrix_base import get_random_matrix
def main():
    x = input(f"What's Matrix Order(eg: 2x3)? ")
    x = x.split("x")
    if len(x) == 2:
        row_len = int(x[0])
        col_len = int(x[1])
        mat = get_random_matrix(row_len, col_len)
    else:
        order = int(x[0])
        mat = get_random_matrix(order)
    
    matrix(mat, "Inverse")

if __name__ == "__main__":
    main()
