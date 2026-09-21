def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # print("Comparing:", left[i], "and", right[j])

        if left[i][2] < right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


employees = [
    (101, "Amit", 45000),
    (102, "Riya", 30000),
    (103, "Kiran", 55000),
    (104, "Bhavya", 40000)
]

ans = merge_sort(employees)

for emp in ans:
    print(emp)
# print(ans)