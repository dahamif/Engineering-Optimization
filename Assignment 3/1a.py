
import numpy as np
import matplotlib.pyplot as plt

# Define a wider range of x
x = np.linspace(-5, 5, 1500)

mu_values = [0, 1, 2, 3]

plt.figure(figsize=(10, 7))

for mu in mu_values:
    # Lagrangian
    L = x**2 + mu * (1 - x)

    # Minimizer
    x_min = mu / 2
    L_min = x_min**2 + mu * (1 - x_min)

    # Plot the curve
    plt.plot(x, L, linewidth=2, label=f'μ = {mu}')

    # Mark the minimum
    plt.scatter(x_min, L_min, color='black', zorder=3)

    plt.annotate(
        f'({x_min:.1f}, {L_min:.2f})',
        (x_min, L_min),
        xytext=(7, 8),
        textcoords='offset points'
    )

plt.xlabel('x', fontsize=12)
plt.ylabel('L(μ, x)', fontsize=12)
plt.title('Lagrangian for Different Values of μ', fontsize=14)

plt.xlim(-5, 5)
plt.ylim(-2, 30)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
