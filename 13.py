def activity_selection(start, finish):
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = 0

    for s, f in activities:
        if s >= last_end:
            selected.append((s, f))
            last_end = f

    return selected


n = int(input("Enter number of activities: "))

start = []
finish = []

for i in range(n):
    s = int(input("Enter start time: "))
    f = int(input("Enter finish time: "))

    start.append(s)
    finish.append(f)

ans = activity_selection(start, finish)

print("Selected activities:", ans)