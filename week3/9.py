import random

n = 10

A = [random.randint(1, 11) for _ in range(n)]

print(A)

B = [1]*n

for i in range(0,n):
    j = 0
    while j < n:
        if j== i:
            j += 1
            continue
        B[i] *= A[j]
        j += 1

print(B)