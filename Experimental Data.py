import numpy as np
import matplotlib.pyplot as plt

# Example experimental data
time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 2, 4, 6, 8, 10])

plt.plot(time, position, 'ro')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Experimental Data: Position vs. Time')
plt.grid(True)
plt.show()
