import numpy as np
import matplotlib.pyplot as plt
import random

def coin_flip(p, n_flips):
    """Simulates n_flips coin flips with probability p of getting heads."""
    return np.sum(np.random.rand(n_flips) < p)

n_experiments = 100
n_flips = 50
p_values = np.arange(0, 1.01, 0.01)
measured_values = np.zeros((len(p_values), n_experiments))
for i, p in enumerate(p_values):
    for j in range(0, n_experiments):
        measured_values[i, j] = coin_flip(p, n_flips)
plt.figure(figsize=(5, 5))
for i in range(0,n_experiments):
    plt.scatter(p_values, measured_values[:,i], c='green', alpha=.2)
plt.plot([0, 1], [0, n_flips], c='r')
plt.xlabel('True probablity of getting heads')
plt.ylabel('Measured probablity of getting heads')
plt.title('Neyman Construction for coin probability')
plt.show()
