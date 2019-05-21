import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(0, 2, 10)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, 4-x**2)        # Plot the sine of each x point
plt.show()                   # Display the plot
