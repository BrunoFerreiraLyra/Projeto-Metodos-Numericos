import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolacao(x, y, x_interp):
    """
    Realiza interpolação de Lagrange para um conjunto de pontos.
    Retorna o valor interpolado em x_interp.
    """
    n = len(x)
    resultado = 0.0

    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (x_interp - x[j]) / (x[i] - x[j])
        resultado += termo

    return resultado

# Exemplo de uso com exibição do resultado e gráfico
if __name__ == "__main__":
    # Pontos conhecidos
    x = [1.0, 2.0, 3.0]
    y = [2.0, 3.0, 5.0]

    # Ponto a interpolar
    x_interp = 2.5
    y_interp = lagrange_interpolacao(x, y, x_interp)

    # Exibir resultado numérico
    print(f"Valor interpolado em x = {x_interp} é {y_interp:.4f}")

    # Gerar pontos para o gráfico
    x_vals = np.linspace(min(x), max(x), 200)
    y_vals = [lagrange_interpolacao(x, y, xi) for xi in x_vals]

    # Plotar gráfico
    plt.plot(x_vals, y_vals, label="Interpolação de Lagrange", color="blue")
    plt.scatter(x, y, color="red", label="Pontos dados")
    plt.scatter(x_interp, y_interp, color="green", label=f"Ponto interpolado ({x_interp}, {y_interp:.2f})")
    plt.title("Interpolação de Lagrange")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
