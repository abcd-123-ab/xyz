def matrix_chain(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = 999999

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

        print("After iteration", length - 1)
        for row in dp:
            print(row)
        print()

    return dp[1][n-1]


arr = [5, 10, 15, 20, 25]

print("Minimum number of multiplications:", matrix_chain(arr))