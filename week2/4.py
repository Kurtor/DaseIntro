target = 2
guess = 1.4
epsilon = 1e-5

while abs(guess * guess - target) > epsilon:
    guess = (guess + target / guess) / 2

print("根号二为:", guess)