# def knapsack(W, benefit, resource, n):
#     dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(W + 1):
#             if resource[i - 1] <= w:
#                 pick = benefit[i - 1] + dp[i - 1][w - resource[i - 1]]
#                 notPick = dp[i - 1][w]
#                 dp[i][w] = max(pick, notPick)
#             else:
#                 dp[i][w] = dp[i - 1][w]

#     return dp[n][W]


# benefit = [10, 15, 20]
# resource = [2, 3, 4]

# W = 6
# n = len(benefit)

# print("Maximum Benefit:", knapsack(W, benefit, resource, n))



def knapsack(W, val, wt, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                pick = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                notPick = dp[i - 1][w]
                dp[i][w] = max(pick, notPick)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


val = [10, 15, 20]
wt = [2, 3, 4]

W = 6
n = len(val)

print("Maximum Benefit:", knapsack(W, val, wt, n))