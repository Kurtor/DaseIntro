import math
x = int(input())
y = int(math.sqrt(x)) + 1
count = 0
for i in range(2, y):
    if x % i == 0:
        print("yes")
        count += 1
        break
if count > 0:
    print("no")
