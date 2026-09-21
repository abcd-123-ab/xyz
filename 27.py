# def matrix_chain(p):
#     n = len(p)
#     dp = [[0] * n for _ in range(n)]

#     for length in range(2, n):
#         for i in range(1, n - length + 1):
#             j = i + length - 1
#             dp[i][j] = 999999

#             for k in range(i, j):
#                 cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
#                 dp[i][j] = min(dp[i][j], cost)

#     return dp[1][n-1]


# arr = [5, 10, 15, 20, 25]

# print("Minimum number of multiplications:", matrix_chain(arr))

mc = [[-1 for n in range(50)] for m in range(50)]

def DynamicProgramming(c, i, j):
    if i == j:
        return 0

    if mc[i][j] != -1:
        return mc[i][j]

    mc[i][j] = 999999

    for k in range(i, j):
        mc[i][j] = min(mc[i][j],
                       DynamicProgramming(c, i, k) +
                       DynamicProgramming(c, k + 1, j) +
                       c[i - 1] * c[k] * c[j])

    return mc[i][j]


def Matrix(c, n):
    i = 1
    j = n - 1
    return DynamicProgramming(c, i, j)


arr = [5, 10, 15, 20, 25]
n = len(arr)

print("Minimum number of multiplications is:")
print(Matrix(arr, n))