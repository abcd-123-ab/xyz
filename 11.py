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


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print("Selected activities:", activity_selection(start, finish))

# def activity(start,end):
#     acti=list(zip(start,end))
#     acti.sort(key=lambda x:x[1])

#     result=[]
#     last=0

#     for s,f in acti:
#         if s>=last:
#             result.append((s,f))
#             last=f

#     return result

# start=[1,3,0,5,8,5]
# finish=[2,4,6,7,9,9]
# print(activity(start,finish))        