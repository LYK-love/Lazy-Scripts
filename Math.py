import numpy as np
import matplotlib.pyplot as plt


# Generate time values with a smaller time step
Ts = 0.0005
t = np.arange(-0.03, 0.05, Ts)  # Smaller time step (0.0001 seconds)

# Compute x(t) using the given equation

x = 20 * np.cos(2 * np.pi * 40 * t - 0.4 * np.pi)

# Plot the function
# plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title(r'$x(t) = 10 \cos(2\pi(440)t - 0.4\pi)$')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
