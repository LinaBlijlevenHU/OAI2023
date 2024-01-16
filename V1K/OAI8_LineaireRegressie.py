import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame(data={'x': [1, 2, 3, 4], 'y': [4, 7, 8, 15]})

# Use Seaborn to create a scatter plot
sns.scatterplot(data=df, x="x", y="y", color="black")
x_values = np.linspace(df['x'].min(), df['x'].max(), 100)

# Plot two lines to compare to the datapoints. What is happening?
# Which is better?
plt.plot(x_values, 3 + 4 * x_values, label='3 + 4x', color='red')
plt.plot(x_values, 4 + 3 * x_values, label='4 + 3x', color='blue')

plt.legend()

# Show the plot
plt.show()
