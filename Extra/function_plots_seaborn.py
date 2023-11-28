import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

# Set Seaborn style
sns.set(style="whitegrid")

# Define the functions
def constant(x):
    return np.ones_like(x)

def linear(x):
    return x

def quadratic(x):
    return x**2

def exponential(x):
    return 2**x

def factorial(x):
    return [math.factorial(val) for val in x]

# Generate x values
x_values = np.arange(0, 51, 10)

# Plot the functions using Seaborn
plt.figure(figsize=(10, 6))  # Set figure size

# Plot with Seaborn and customize style
sns.lineplot(x=x_values, y=constant(x_values), label='Constant (y=1)', color='blue', marker='o')
sns.lineplot(x=x_values, y=linear(x_values), label='Linear (y=n)', color='green', marker='s')
sns.lineplot(x=x_values, y=quadratic(x_values), label='Quadratic (y=n^2)', color='red', marker='^')
sns.lineplot(x=x_values, y=exponential(x_values), label='Exponential (y=2^n)', color='purple', marker='D')
sns.lineplot(x=x_values, y=factorial(x_values), label='Factorial (y=n!)', color='orange', marker='o')

# Add labels and legend inside the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Different Functions')
plt.legend(loc='upper left')

# Show the plot
plt.show()
