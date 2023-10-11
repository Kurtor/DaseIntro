#经过检索知乎和gpt辅助思路
#同等层数下阿基米德方法应该最佳
import math
import random

def calculate_pi_leibniz(n):
    pi_estimate = 0
    sign = 1

    for i in range(n):
        pi_estimate += sign * 1 / (2 * i + 1)
        sign *= -1

    return 4 * pi_estimate

def calculate_pi_montecarlo(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

def calculate_pi_archimedes(num_sides):
    radius = 1
    side_length = 2 * radius * math.sin(math.pi / num_sides)
    polygon_perimeter = num_sides * side_length
    pi_estimate = polygon_perimeter / (2 * radius)

    return pi_estimate

target_pi = round(math.pi, 10)

n = 10000  # leibniz
num_samples = 10000  # montecarlo
num_sides = 10000  # archimedes

pi_leibniz = calculate_pi_leibniz(n)
pi_monte_carlo = calculate_pi_montecarlo(num_samples)
pi_archimedes = calculate_pi_archimedes(num_sides)

print("leibniz估计π:", pi_leibniz, "误差:", abs(pi_leibniz - target_pi))
print("montecarlo估计π:", pi_monte_carlo, "误差:", abs(pi_monte_carlo - target_pi))
print("archimedes估计π:", pi_archimedes, "误差:", abs(pi_archimedes - target_pi))
