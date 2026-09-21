def fractional_knapsack(capacity, weight, values, name):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weight[i]
        items.append((ratio, values[i], weight[i], name[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, value, weight, name in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            print(name, "=> Full item")
        else:
            fraction = capacity / weight
            total_value += ratio * capacity

            print(name, "=> Fraction:", fraction)
            break

    return total_value


name = ["Item1", "Item2", "Item3"]
values = [60, 100, 120]
weight = [10, 20, 30]

capacity = 40

result = fractional_knapsack(capacity, weight, values, name)

print("Maximum value:", result)