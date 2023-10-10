x = float(input())
print("0.", end = '')
while x - int(x) > 0 :
    x = x * 2
    print(f"{int(x)}", end = '')
    x = x - int(x)



