
import numpy as np
import matplotlib.pyplot as plt

# Optimal primal and dual solutions
x_star = 1
mu_star = 2

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Graph 1: L(mu, x*) against mu
mu = np.linspace(0, 5, 500)
L1 = x_star**2 + mu * (1 - x_star)

axes[0].plot(mu, L1, linewidth=2.5, color='blue')
axes[0].axhline(1, color='red', linestyle='--',
                label=r'$L(\mu^*,x^*)=1$')
axes[0].scatter(mu_star, 1, color='red', s=65, zorder=3)

axes[0].set_xlabel(r'$\mu$', fontsize=12)
axes[0].set_ylabel(r'$L(\mu,x^*)$', fontsize=12)
axes[0].set_title(r'$L(\mu,x^*)$ against $\mu$')
axes[0].set_xlim(0, 5)
axes[0].set_ylim(0, 2)
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend()

# Graph 2: L(mu*, x) against x
x = np.linspace(-1, 3, 500)
L2 = x**2 + mu_star * (1 - x)

axes[1].plot(x, L2, linewidth=2.5, color='blue')
axes[1].axhline(1, color='red', linestyle='--',
                label=r'$L(\mu^*,x^*)=1$')
axes[1].scatter(x_star, 1, color='red', s=65, zorder=3)

axes[1].set_xlabel('$x$', fontsize=12)
axes[1].set_ylabel(r'$L(\mu^*,x)$', fontsize=12)
axes[1].set_title(r'$L(\mu^*,x)$ against $x$')
axes[1].set_xlim(-1, 3)
axes[1].set_ylim(0, 6)
axes[1].grid(True, linestyle='--', alpha=0.5)
axes[1].legend()

plt.tight_layout()
plt.show()
