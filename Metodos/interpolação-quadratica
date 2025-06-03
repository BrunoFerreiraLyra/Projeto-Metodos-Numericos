import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])

A = np.array([[1, x[0], x[0]**2],
              [1, x[1], x[1]**2],
              [1, x[2], x[2]**2]])

coef = np.linalg.solve(A, y)
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])

A = np.array([[1, x[0], x[0]**2],
              [1, x[1], x[1]**2],
              [1, x[2], x[2]**2]])

coef = np.linalg.solve(A, y)

def P(x):
    return coef[0] + coef[1]*x + coef[2]*x**2

x_interp = 2.5
y_interp = P(x_interp)
print(f"Valor interpolado em x = {x_interp}: {y_interp:.4f}")

x_vals = np.linspace(0.5, 3.5, 100)
y_vals = P(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Polinômio Interpolador', color='blue')
plt.scatter(x, y, color='red', label='Pontos Dados', zorder=5)
plt.scatter(x_interp, y_interp, color='green', label=f'Interpolado (x={x_interp})', zorder=5)
plt.title('Interpolação Quadrática')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
