# arr = list(x for x in range(1,4))
# print(arr)
# while (len(arr) > 5):
#     len (arr+1)s
#     arr[4+1]=arr[4]
#     arr.pop()
#     for x in arr:
#         print(x, end=" ")

inc = 1
row_tot = 3
for i in range(0,4):
    k = 0
    if i >= 1:
        inc = -1
    while k < row_tot:
        k += 1
        print("#", end=" ")
    row_tot += inc
    print("")

