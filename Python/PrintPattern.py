#arr = list(input("Enter the numbers separated by space : ").split(" "))
arr = list(x for x in range(1,8))
#print(arr)
while (len(arr) > 3):
    for x in arr:
        print(x, end=" ")
    print("")
    arr.pop()
    