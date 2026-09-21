def fractional_knapsack(capacity, weight, values):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weight[i]
        items.append((ratio, values[i], weight[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, value, weight in items:
        if capacity >= weight:
            capacity -= weight
            profit += value
        else:
            profit += ratio * capacity
            break

    return profit


values = [100, 60, 120]
weight = [20, 10, 30]
capacity = 50

profit = fractional_knapsack(capacity, weight, values)

print("Maximum Profit:", profit)