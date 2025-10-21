import numpy as np
import matplotlib.pyplot as plt
from por_engine.por_kernel import por

# Параметри
S, H, T = 0.9, 0.85, 1.0
alphas = np.linspace(0.8, 2.0, 25)   # 25 кроків по α
distances = np.logspace(0, -3, 25)   # D = 1 → 0.001 (логарифмічна шкала)

# Обчислення PoR для кожної комбінації
heatmap = np.zeros((len(alphas), len(distances)))
for i, alpha in enumerate(alphas):
    for j, D in enumerate(distances):
        heatmap[i, j] = por(S, H, T, D, alpha)

# Візуалізація
plt.figure(figsize=(8, 6))
plt.imshow(
    heatmap,
    extent=[distances.min(), distances.max(), alphas.min(), alphas.max()],
    aspect='auto',
    origin='lower',
    cmap='plasma'
)
plt.colorbar(label='PoR Intensity')
plt.xscale('log')
plt.xlabel('Cognitive Distance (D)')
plt.ylabel('Non-linearity (α)')
plt.title('Resonant Intensity Heatmap (RSP Stability Field)')
plt.tight_layout()
plt.show()
