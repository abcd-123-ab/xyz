def fractional_knapsack(capacity, weight, values, name):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weight[i]
        items.append((ratio, values[i], weight[i], name[i]))

    items.sort(reverse=True)

    total_value = 0

    print("Items selected:")

    for ratio, value, weight, name in items:

        if capacity >= weight:
            capacity -= weight
            total_value += value

            print(name, "-> Full item")
            print("Weight:", weight, "Value:", value)
            print("Remaining capacity:", capacity)

        else:
            total_value += ratio * capacity

            print(name, "-> Fraction item")
            print("Weight taken:", capacity)
            print("Value taken:", total_value)

            capacity = 0
            break

    print("Total value:", total_value)


name = ["Silver", "Platinum", "Gold"]
values = [100, 60, 120]
weight = [20, 10, 30]
capacity = 50

fractional_knapsack(capacity, weight, values, name)