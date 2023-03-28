import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def my_func(x):
    f=4*(x**2) - 4*x + 4
    return f

# Generate x values to plot the function
xVal = np.linspace(-5, 6, 80)

# Calculate the function values at the x values
yVal = my_func(xVal)

# Find the minimum of the function
Min = optimize.minimize(my_func, x0=0)

print("The minimum of the function found at x =", Min.x[0])
print("The minimum value =", Min.fun)

# Plot the function and the minimum
plt.plot(xVal, yVal, color= 'green', label="Function")
plt.plot(Min.x, Min.fun, "-p", color='black', label="Minimum")
plt.title("Minimum of $4x^2-4x+4$")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()



