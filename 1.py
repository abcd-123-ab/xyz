# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left,right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# array = [1, 33, 5, 99, 0, 12, 7, 45, 23, 8]

# print("Original array:", array)

# ans = merge_sort(array)

# print("Sorted array:", ans)


def merge(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=merge(arr[:mid])
    right=merge(arr[mid:])

    return m(left,right)

def m(left,right):
    i=j=0
    result=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:

            result.append(left[i])
            i+=1
        else:
            result.append(right[j]) 
            j+=1


    result.extend(left[i:])
    result.extend(right[j:])

    return result

array=[2,5,4,8,6,1,99,3,23]
print("original Array:",array)
ans=merge(array)
print("final array",ans)           
        
