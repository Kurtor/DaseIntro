target = 2000
guess = 45
epsilon = 1e-5

while abs(guess * guess - target) > epsilon:
    guess = (guess + target / guess) / 2

print("根号2000为:", guess)

#在设置成2000之时，相应的初始guess也应当适当调整以减少循环次数