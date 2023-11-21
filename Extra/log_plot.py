import matplotlib.pyplot as plt
import numpy as np

# Generate dummy data
leeftijden = [x for x in np.linspace(18, 65, 100)]
inkomens = [x for x in np.linspace(20000, 100000, 100)]

# Voeg outlier toe
leeftijden.append(55)
inkomens.append(2000000000)

for i in range(len(leeftijden)):
    print(f"Leeftijd: {leeftijden[i]}, Inkomens: {inkomens[i]}")

# Plot with linear axes
plt.subplot(1, 2, 1)
plt.scatter(leeftijden, inkomens, label='Linear Scale')
plt.title('Linear Scale')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Plot with logarithmic axes
plt.subplot(1, 2, 2)
plt.scatter(leeftijden, inkomens, label='Logarithmic Scale')
plt.xscale('log')
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.xlabel('X-axis (log scale)')
plt.ylabel('Y-axis (log scale)')
plt.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()