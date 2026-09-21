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


start = [9, 10, 11, 12, 13, 14]
finish = [10, 11, 12, 13, 14, 15]

ans = activity_selection(start, finish)

print("Selected classes:", ans)
print("Maximum classes:", len(ans))