def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

temp =0
for x in range (10, 1000):
    if is_prime(x):
        temp =temp+x

print(temp)