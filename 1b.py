import numpy as np
import matplotlib.pyplot as plt

# Dual variable
mu = np.linspace(0, 5, 1000)

# Dual function: d(mu) = mu - mu^2/4
d = mu - mu**2 / 4

# Plot
plt.figure(figsize=(9, 6))
plt.plot(mu, d, linewidth=2.5, color='blue')

plt.xlabel(r'$\mu$', fontsize=12)
plt.ylabel(r'$d(\mu)$', fontsize=12)
plt.title('Dual Function', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 5)
plt.ylim(-2, 1.3)


plt.tight_layout()
plt.show()