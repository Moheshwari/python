# Remove 2 and add 3 to the list and replace True with False.
# Li = [1,3,5, [2,3], True]
# Output = [1,3,5, [3,3], False]

Li = [1,3,5, [2,3], True]
Li[3][0] = 3
Li[4] = False
print(Li)
