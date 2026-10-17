
import numpy as np
import matplotlib.pyplot as plt

# Feasible region: x >= 1
x = np.linspace(1, 3, 500)
g = x**2

plt.figure(figsize=(9, 6))

# Plot g(x) for feasible x
plt.plot(x, g, linewidth=2.5, color='blue',
         label=r'$g(x)=x^2,\quad x\geq1$')


# Indicate infeasible region
plt.axvspan(-1, 1, color='orange', alpha=0.15,
            label=r'Infeasible: $g(x)=+\infty$')

plt.text(0, 6,
         r'$g(x)=+\infty$ for $x<1$',
         fontsize=12, ha='center')

plt.xlabel('$x$', fontsize=12)
plt.ylabel('$g(x)$', fontsize=12)
plt.title('Primal Function', fontsize=14)

plt.xlim(-1, 3)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
