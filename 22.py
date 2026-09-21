def knapsack(W, val, wt):
    n = len(val)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                pick = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                notPick = dp[i - 1][w]
                dp[i][w] = max(pick, notPick)
            else:
                dp[i][w] = dp[i - 1][w]

    print("DP Table:")
    for row in dp:
        print(row)

    return dp[n][W]


val = [1, 7, 11]
wt = [1, 2, 3]
W = 5

print("Maximum Profit:", knapsack(W, val, wt))