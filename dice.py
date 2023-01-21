import random
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to the dice simulation!")
num_dice = int(input("How many dice would you like to roll? "))

rolls = []
for i in range(num_dice):
    rolls.append(random.randint(1, 6))

plt.hist(rolls, bins=range(1, 7), density=True)

# Calculate and plot normal distribution
mean = 3.5 # mean of the fair dice
stddev = np.sqrt(mean*(6-1)/6)  # standard deviation for fair dice
x = np.linspace(1, 6, 100)
plt.plot(x, 1/(stddev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * stddev**2) ), linewidth=2)

plt.show()
