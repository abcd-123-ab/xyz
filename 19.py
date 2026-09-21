def fractional_knapsack(capacity, weight, values, name):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weight[i]
        items.append((ratio, values[i], weight[i], name[i]))

    items.sort(reverse=True)

    total_return = 0

    for ratio, value, weight, name in items:
        if capacity >= weight:
            capacity -= weight
            total_return += value
            print(name, "=> Investment-", weight,", Return-", value)
        else:
            remaining = ratio * capacity
            total_return += remaining

            print(name, "=> Partial Investment-", capacity,", Return-", remaining)
            break

    return total_return


name = ["Project A", "Project B", "Project C"]
values = [60,100, 120]
weight = [10,20,30]

capacity = 50

result = fractional_knapsack(capacity, weight, values, name)

print("Maximum Return:", result)