#在不同的初始guess之下，在误差允许范围之内（即epsilon）数值相等
target = 2
guess = 1
epsilon = 1e-5

while abs(guess * guess - target) > epsilon:
    guess = (guess + target / guess) / 2

print("根号二为:", guess)

target = 2
guess = 2
epsilon = 1e-5

while abs(guess * guess - target) > epsilon:
    guess = (guess + target / guess) / 2

print("根号二为:", guess)

target = 2
guess = 0.25
epsilon = 1e-5

while abs(guess * guess - target) > epsilon:
    guess = (guess + target / guess) / 2

print("根号二为:", guess)