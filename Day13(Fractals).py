import numpy as np
import matplotlib.pyplot as plt

width, height = 1000, 1000
max_iterations = 100

x = np.linspace(-2, 2, width)
y = np.linspace(-2, 2, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

iterations = np.zeros(Z.shape, dtype=int)

C = Z.copy()
for i in range(max_iterations):
    Z = Z**100+ C
    mask = np.abs(Z) < 1000
    iterations += mask

plt.figure(figsize=(10, 10))
plt.imshow(iterations, extent=(-2, 2, -2, 2), cmap='hot', origin='lower')
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()