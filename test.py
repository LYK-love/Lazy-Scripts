
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

if __name__ == "__main__":
    Ts = 0.01  # units are seconds
    duration = 0.3
    tt = np.arange(0, duration, Ts)
    Fo = 380  # units are Hz
    xn = 2 * np.cos(2 * np.pi * Fo * tt + 0.6 * np.pi)
    f = plt.figure()
    plt.stem(np.arange(len(xn)), xn)
    plt.grid(True)
    plt.show()