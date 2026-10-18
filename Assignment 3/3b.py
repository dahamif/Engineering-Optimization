
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(0, 5, 500)

# Lagrangian for x = 0, 1, 2
L_x0 = mu
L_x1 = np.ones_like(mu)
L_x2 = 4 - mu

# Lower envelope
d_approx = np.minimum.reduce([L_x0, L_x1, L_x2])

plt.plot(mu, L_x0, label=r'$x=0: L(\mu,0)=\mu$')
plt.plot(mu, L_x1, label=r'$x=1: L(\mu,1)=1$')
plt.plot(mu, L_x2, label=r'$x=2: L(\mu,2)=4-\mu$')
plt.plot(mu, d_approx, 'k--', linewidth=2,
         label='Lower envelope')

plt.xlabel(r'$\mu$')
plt.ylabel(r'$L(\mu,x)$')
plt.title('Lagrangian Lines and Lower Envelope')
plt.xlim(0, 5)
plt.ylim(-2, 5)
plt.xticks(np.arange(0, 6, 1))
plt.grid(True)
plt.legend()
plt.show()
