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

m = int(input('Nhap chieu cao: '))
pascal(m)


