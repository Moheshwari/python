# Input a list from the user then Remove duplicates from a list and create a set and find the max
# number. User_input = [1,9,3,4,5,200,54]

user_input = list (input("Enter the values : ").split(","))
S = set()
for i in range(len(user_input)):
    if user_input[i] not in S:
        S.add(user_input[i])

print(S)
