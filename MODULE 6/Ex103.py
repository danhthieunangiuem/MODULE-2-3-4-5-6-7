m = int(input('Nhap chieu cao: '))
def pascal(m):
    n = 2 * m + 1
    mid = n // 2
    A = [[0 for _ in range(n)] for _ in range(m)]
    A[m - 1][mid] = 1
    for i in range(m - 2, -1, -1):
        for j in range(1, n - 1):
            A[i][j] = A[i + 1][j - 1] + A[i + 1][j + 1]
            if A[i][j-1] > 1:
                A[i][j-1] +=1

    for i in range(m):
        for j in range(n):
            if A[i][j] != 0:
                print(f"{A[i][j]} ", end="")
            else:
                print("  ", end="")
        print()

pascal(m)
def pascal2(m):
    n = 2*m+1
    mid = n // 2
    A = [[0 for _ in range(m)] for _ in range(n)]

    A[mid][0] = 1

    for j in range(1, m): #cot :m
        for i in range(n): #dong:n
            if i < n - 1:
                A[i][j] += A[i - 1][j - 1]
                A[i][j] += A[i + 1][j - 1]

    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                print(f"{A[i][j]} ", end="")
            else:
                print("  ", end="")
        print()

pascal2(m)
def pascal3(m):
    n = 2*m+1
    mid = n // 2
    A = [[0 for _ in range(m)] for _ in range(n)]
    A[mid][m-1] = 1
    for j in range(m, 0, -1): #cot :m
        for i in range(n-1): #dong:n
            if j < m:
                A[i][j-1] += (A[i - 1][j])
                A[i][j-1] += (A[i + 1][j])
            if A[i][j-1] > 1:
                A[i][j-1] +=1
    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                print(f"{A[i][j]:2d}", end="")
            else:
                print("  ", end="")
        print()
pascal3(m)


