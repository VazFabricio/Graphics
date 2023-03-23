import matplotlib.pyplot as plt
from time import sleep

# Define a lista de números
numeros = [34, 31, 22, 36, 2, 20, 15, 11, 25, 37, 43, 35, 6, 41, 28, 1, 32, 50, 18, 29, 38, 8, 47, 23, 10, 40, 5, 21, 7, 30, 48, 33, 26, 13, 49, 12, 9, 39, 17, 19, 44, 3, 24, 16, 42, 46, 45, 27, 4, 14]

# Plota o gráfico inicial
plt.bar(range(len(numeros)), numeros)
plt.show()

# Implementa o algoritmo de ordenação (bubble sort)
for i in range(len(numeros)):
    for j in range(len(numeros)-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            # Atualiza o gráfico
            plt.clf()  # Limpa o gráfico anterior
            plt.bar(range(len(numeros)), numeros)  # Plota o novo gráfico
            plt.bar(j, numeros[j], color='red')  # Exibe a barra atual em vermelho
            plt.bar(j+1, numeros[j+1], color='red')  # Exibe a barra seguinte em vermelho
            plt.draw()  # Desenha o novo gráfico
            plt.pause(0.0001)  # Intervalo de tempo entre as atualizações
            plt.bar(j, numeros[j])  # Remove a cor vermelha da barra atual
            plt.bar(j+1, numeros[j+1])  # Remove a cor vermelha da barra seguinte

# Plota o gráfico final
plt.bar(range(len(numeros)), numeros)
plt.show()