import numpy as np
import matplotlib.pyplot as plt

coefficients = [1, -0.5, 0.5, -1]

roots = np.roots(coefficients)

print("Roots of P(z):")
for root in roots:
    print(root)

# Plot the roots in the complex plane
plt.figure(figsize=(6, 6))
plt.scatter(np.real(roots), np.imag(roots), color='red', marker='x')
plt.axvline(0, color='black', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.title('Roots of P(z)')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.show()



