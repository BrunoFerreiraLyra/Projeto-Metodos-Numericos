import numpy as np
import matplotlib.pyplot as plt
import time
# -------------------------
# 1. Dados reais
# -------------------------
# Vetor de horários (x) e temperaturas (y)
x = np.array([10, 12, 14])
y = np.array([22, 26, 28])

# Ponto a ser interpolado
x_interp = 11

# -------------------------
# 2. Função de interpolação linear
# -------------------------
def interpolacao_linear(x0, y0, x1, y1, x):
    return y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)

# -------------------------
# 3. Encontrar intervalo correto
# -------------------------
for i in range(len(x) - 1):
    if x[i] <= x_interp <= x[i + 1]:
        x0, x1 = x[i], x[i + 1]
        y0, y1 = y[i], y[i + 1]
        break

# -------------------------
# 4. Calcular interpolação e medir tempo
# -------------------------
start = time.time()
y_interp = interpolacao_linear(x0, y0, x1, y1, x_interp)
end = time.time()

# -------------------------
# 5. Mostrar resultado no terminal
# -------------------------
print(f"Temperatura aproximada às {x_interp}h: {y_interp:.2f} °C")
print(f"Tempo de execução: {(end - start) * 1000:.5f} ms")

# -------------------------
# 6. Gerar gráfico
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o-', label='Dados reais')
plt.plot(x_interp, y_interp, 'r*', markersize=12, label=f'Interpolado: {y_interp:.2f}°C às {x_interp}h')
plt.title('Interpolação Linear da Temperatura')
plt.xlabel('Hora do Dia')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
