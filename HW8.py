import numpy as np
import matplotlib.pyplot as plt


def coin_flip(p, n_flips):
    "Simulates N_flips coin flips with probability p of getting heads"
    flips = np.random.rand(n_flips) < p
    return np.sum(flips)
 

N_experiments = 100
N_flips = 50
p_values = np.linspace(0, 1, 101)
measured_values = np.zeros((len(p_values), N_experiments))

for j in range(N_experiments):
    measured_values[:, j] = np.array([coin_flip(p, N_flips) for p in p_values])

plt.figure(figsize=(5, 5))
for i in range(0,N_experiments):
    plt.scatter(p_values, measured_values[:,i], c='green', alpha=.2)

plt.plot([0, 1], [0, N_flips], c='r')
plt.xlabel('True probablity of getting heads')
plt.ylabel('Measured probablity of getting heads')
plt.title('Neyman Construction for coin probability')
plt.show()
