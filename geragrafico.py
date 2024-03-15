
from leitorarquivo import leitorarquivo
import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = leitorarquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')

    plt.title('Gráfico de linhas')

    plt.plot(valores)
    plt.show()


main()

