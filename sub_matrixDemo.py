def main():
    from matrix_base import get_matrix, print_matrix
    #from matrix_properties import sub_matrix
    from display import matrix

    m = get_matrix(4)
    print_matrix(m)
    print()

    matrix(m)

if __name__ == "__main__":
    main()