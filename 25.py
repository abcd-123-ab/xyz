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

    return dp[n][W]


def greedy(W, val, wt):
    items = []

    for i in range(len(val)):
        ratio = val[i] / wt[i]
        items.append((ratio, val[i], wt[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, value, weight in items:
        if weight <= W:
            W = W - weight
            profit = profit + value

    return profit


val = [1, 7, 11]
wt = [1, 2, 3]
W = 5

dp_result = knapsack(W, val, wt)
greedy_result = greedy(W, val, wt)

print("0/1 Knapsack (DP):", dp_result)
print("Greedy:", greedy_result)