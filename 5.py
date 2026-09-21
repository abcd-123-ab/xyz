def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = merge(left, right)

    print("After merge:", result)

    return result


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


array = [1, 33, 5, 99, 0]

print("Original:", array)

ans = merge_sort(array)

print("Final sorted array:", ans)