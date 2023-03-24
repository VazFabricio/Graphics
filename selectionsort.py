import matplotlib.pyplot as plt
from time import sleep

# Define a lista de números
numeros = [34, 31, 22, 36, 2, 20, 15, 11, 25, 37, 43, 35, 6, 41, 28, 1, 32, 50, 18, 29, 38, 8, 47, 23, 10, 40, 5, 21, 7, 30, 48, 33, 26, 13, 49, 12, 9, 39, 17, 19, 44, 3, 24, 16, 42, 46, 45, 27, 4, 14]

# Plota o gráfico inicial
plt.bar(range(len(numeros)), numeros)
plt.show()

# Implementa o algoritmo de ordenação (selection sort)
for i in range(len(numeros)):
    # Encontra o menor elemento a partir da posição atual
    min_index = i
    for j in range(i+1, len(numeros)):
        if numeros[j] < numeros[min_index]:
            min_index = j
            
    # Troca o menor elemento com o elemento atual
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]
    
        # Atualiza o gráfico
    plt.clf()  # Limpa o gráfico anterior
    plt.bar(range(len(numeros)), numeros)  # Plota o novo gráfico
    plt.bar(j, numeros[j], color='red')  # Exibe a barra atual em vermelho
    plt.bar(i, numeros[min_index], color='green')
    plt.draw()  # Desenha o novo gráfico
    plt.pause(0.1)  # Intervalo de tempo entre as atualizações

# Plota o gráfico final
plt.bar(range(len(numeros)), numeros)
plt.show()
