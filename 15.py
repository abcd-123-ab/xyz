# def activity_selection(start, finish):
#     activities = list(zip(start, finish))
#     activities.sort(key=lambda x: x[1])

#     selected = []
#     last_end = 0

#     for s, f in activities:
#         if s >= last_end:
#             selected.append((s, f))
#             last_end = f

#     return selected


# start = [1, 3, 0, 5, 8, 5]
# finish = [2, 4, 6, 7, 9, 9]

# ans = activity_selection(start, finish)

# print("Selected meetings:", ans)
# print("Maximum meetings:", len(ans))


def activity_selection(start, finish):
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = 0

    for s, f in activities:

        print("Checking:", (s, f))

        if s >= last_end:
            selected.append((s, f))
            last_end = f
            print("Selected:", (s, f))
            print("-"*20)
        else:
            print("Rejected:", (s, f))
            print("-"*20)

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

ans = activity_selection(start, finish)

print("Selected meetings:", ans)
print("Maximum meetings:", len(ans))