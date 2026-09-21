def fractional_knapsack(capacity, weight, values, name):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weight[i]
        items.append((ratio, values[i], weight[i], name[i]))

    items.sort(reverse=True)

    total_value = 0.0

    for ratio, value, weight, name in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            print(name, "=> weight-", weight, ", value-", value)
        else:
            total_value +=  ratio * capacity
            print(name, "=> weight-", capacity, ", value-", total_value)
            break

    return total_value


name = ["silver", "platinum", "gold"]
values = [100, 60, 120]
weight = [20, 10, 30]
capacity = 50

result = fractional_knapsack(capacity, weight, values, name)

print("Maximum value:", result)