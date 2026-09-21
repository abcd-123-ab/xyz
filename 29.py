def matrix(p, i, j):
    if i == j:
        return 0

    dp[i][j] = 999999

    for k in range(i, j):
        cost = (matrix(p, i, k) +
                matrix(p, k + 1, j) +
                p[i - 1] * p[k] * p[j])

        dp[i][j] = min(dp[i][j], cost)

    return dp[i][j]


n = int(input("Enter number of matrices: "))

arr = []

for i in range(n + 1):
    arr.append(int(input("Enter dimension: ")))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

print("Minimum number of multiplications:", matrix(arr, 1, n))