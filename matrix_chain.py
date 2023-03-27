def MatrixChainOrder(p):
    pass


# Print order of matrix with Ai as Matrix
def PrintOptimalSolution(s, i, j):
    pass


def main():
    matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
    # Size of matrix created from above array will be
    # 30*35 35*15 15*5 5*10 10*20 20*25
    n = len(matrix_dimensions)

    Matrix, OptimalSolution = MatrixChainOrder(matrix_dimensions)
    print(Matrix[1][n-1])
    PrintOptimalSolution(OptimalSolution, 1, n - 1)

if __name__ == "__main__":
    main()
