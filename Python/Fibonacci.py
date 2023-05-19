List = [0 for x in range(15)]
print(List)

List[0] = 0
List[1] = 1

for i in range(2,15):
    List[i] = List[i-1] + List[i-2]

print(List)