import random
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to the coin toss simulation!")
num_tosses = int(input("How many times would you like to toss the coin? "))

tosses = []
for i in range(num_tosses):
    tosses.append(random.choice(['Heads', 'Tails']))

plt.hist(tosses, bins=['Heads', 'Tails'], density=True)

# Calculate and plot normal distribution
mean = 0.5  # Assume fair coin
stddev = np.sqrt(mean * (1 - mean))  # Standard deviation for binomial distribution
x = np.linspace(0, 1, 100)
plt.plot(x, 1/(stddev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * stddev**2) ), linewidth=2)

plt.show()
