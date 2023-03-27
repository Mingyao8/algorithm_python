def MatrixChainOrder(p):
    n = len(p)
    s = {}
    m = {}
    for i in range(1, n):
        m[tuple([i, i])] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[tuple([i, j])] = float('inf')
            for k in range(i, j):
                q = m[tuple([i, k])] + m[tuple([k + 1, j])] + (p[i - 1] * p[k] * p[j])
                if q < m[tuple([i, j])]:
                    m[tuple([i, j])] = q
                    s[tuple([i, j])] = k
    return m, s
    pass

def PrintOptimalSolution(OptimalSolution, i, j):
    if i == j:
        print("A{}".format(i), end='')
    else:
        print('(', end='')
        PrintOptimalSolution(OptimalSolution, i, OptimalSolution[tuple([i, j])])
        PrintOptimalSolution(OptimalSolution, OptimalSolution[tuple([i, j])] + 1, j)
        print(')', end='')
    pass


def MemoizedMatrixChain(p):
    n = len(p) - 1
    m = [[0 for x in range(2*n+1)] for x in range(2*n+1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[i][j] = float("inf")
    return LookupChain(m, p, 1, n)

def LookupChain(m, p, i, j):
    n = len(p) - 1
    if m[i][j] < float("inf"):
        return m
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            m1 = LookupChain(m, p, i, k)
            m2 = LookupChain(m, p, k+1, j)
            q = m1[i][k] + m2[k + 1][j] + p[i-1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q
                m[i+n][j+n] = k
    return m

def main():
    matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]

    n = len(matrix_dimensions)
    Matrix, OptimalSolution = MatrixChainOrder(matrix_dimensions)
    List = [(k, v) for k, v in Matrix.items()]
    print(List[-1][1])
    PrintOptimalSolution(OptimalSolution, 1, n - 1)
    print("")  
    m1 = MemoizedMatrixChain(matrix_dimensions)
    print(m1[1][n-1])
    PrintOptimalSolution(m1, 1, n - 1)

if __name__ == "__main__":
    main()

