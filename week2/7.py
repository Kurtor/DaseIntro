target = 10
guess = 1.0
epsilon = 1e-5

while abs(guess**3 - target) > epsilon:
    guess = guess - (guess**3 - target) / (3 * guess**2)

print("10的立方根为:", guess)
