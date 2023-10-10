x = int(input())
y = int(input())
Max = max(x, y)
Min = min(x, y)
temp = Max % Min
while temp != 0:
    Max = Min
    Min = temp
    temp = Max % Min
print(f"{Min}");
