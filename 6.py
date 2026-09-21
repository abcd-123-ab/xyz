# def quick_sort(arr, low, high):
#     if low < high:
#         pivot = partition(arr, low, high)

#         quick_sort(arr, low, pivot - 1)
#         quick_sort(arr, pivot + 1, high)


# def partition(arr, low, high):
#     pivot = arr[low]      
#     i = low + 1
#     j = high

#     while True:

#         while i <= high and arr[i] <= pivot:
#             i += 1

#         while j >= low and arr[j] > pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break

#     arr[low], arr[j] = arr[j], arr[low]

#     return j


# arr = [5, 0, 7, 1, 3]

# print("Original array:", arr)

# quick_sort(arr, 0, len(arr) - 1)

# print("Sorted array:", arr)



def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):
    pivot = arr[high]       # LAST ELEMENT AS PIVOT
    i = low
    j = high - 1

    while True:

        while i <= high - 1 and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[i], arr[high] = arr[high], arr[i]

    return i


arr = [5, 0, 7, 1, 3]

print("Original:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted:", arr)      
