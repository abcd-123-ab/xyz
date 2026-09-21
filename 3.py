count = 0

def merge_sort(arr):
    # global count

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global count
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        count += 1

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [4.5, 2.1, 8.7, 1.3, 6.2,
           9.8, 3.4, 7.6, 5.5, 0.9,
           2.8, 6.7, 4.1, 8.2, 1.5]

print("Original:", numbers)

ans = merge_sort(numbers)

print("Sorted:", ans)
print("Number of comparisons:", count)