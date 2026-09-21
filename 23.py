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


n = int(input("Enter number of items: "))

val = []
wt = []

for i in range(n):
    val.append(int(input("Enter profit: ")))
    wt.append(int(input("Enter weight: ")))

W = int(input("Enter capacity: "))

print("Maximum Profit:", knapsack(W, val, wt, n))
