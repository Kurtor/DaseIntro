import random
import math


def montecarlo(func, a, b, samples):
    total = 0.0
    for _ in range(samples):
        x = random.uniform(a, b)
        total += func(x)

    average = total / samples
    num = average * (b - a)
    return num


# f（）
def target(x):
    return x ** 2 + 4 * x * math.sin(x)


a = 2
b = 3
samples = 100000

estimated_num = montecarlo(target, a, b, samples)
print(estimated_num)