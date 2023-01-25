import random
import matplotlib.pyplot as plt
import numpy as np


class CoinFlipSimulation:
    def __init__(self, num_flips):
        self.num_flips = num_flips
        self.face_count = [0, 0]
        self.probabilities = {}

    @property
    def run_simulation(self):
        for i in range(self.num_flips):
            flip = random.randint(0, 1)
            self.face_count[flip] += 1
        self.probabilities = {'heads': self.face_count[0] / self.num_flips, 'tails': self.face_count[1] / self.num_flips}
        return self.probabilities

    @property
    def plot_normal_distribution(self):
        mu, std = np.mean(list(self.probabilities.values())), np.std(list(self.probabilities.values()))
        s = np.random.normal(mu, std, 1000)
        return s

a = CoinFlipSimulation(100)
a.plot_normal_distribution
