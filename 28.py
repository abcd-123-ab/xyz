dp = [[0 for _ in range(50)] for _ in range(50)]
s = [[0 for _ in range(50)] for _ in range(50)]

def matrix(p, i, j):
    if i == j:
        return 0

    dp[i][j] = 999999

    for k in range(i, j):
        cost = (matrix(p, i, k) +
                matrix(p, k + 1, j) +
                p[i - 1] * p[k] * p[j])

        if cost < dp[i][j]:
            dp[i][j] = cost
            s[i][j] = k

    return dp[i][j]


def printMatrix(i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        printMatrix(i, s[i][j])
        printMatrix(s[i][j] + 1, j)
        print(")", end="")


arr = [5, 10, 15, 20, 25]

n = len(arr)

matrix(arr, 1, n - 1)

print("Optimal Parenthesization:")
printMatrix(1, n - 1)

print()
print("Minimum Multiplications:", dp[1][n - 1])