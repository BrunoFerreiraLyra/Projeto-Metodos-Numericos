import numpy as np
import matplotlib.pyplot as plt

def newton_dif_divididas(x, y, xi):
    n = len(x)
    coef = np.copy(y)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])

    def newton_poly(xi_val):
        result = coef[0]
        for i in range(1, n):
            term = coef[i]
            for j in range(i):
                term *= (xi_val - x[j])
            result += term
        return result

    return np.array([newton_poly(xi_val) for xi_val in xi])

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 0, 5])

xi = np.linspace(min(x), max(x), 100)

yi = newton_dif_divididas(x, y, xi)

plt.figure(figsize=(8, 5))
plt.plot(xi, yi, label='Interpolação de Newton', color='blue')
plt.scatter(x, y, color='red', label='Pontos Originais')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Newton (Diferenças Divididas)')
plt.legend()
plt.grid(True)
plt.show()
