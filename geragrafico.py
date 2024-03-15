
from leitorarquivo import leitorarquivo


def main():
    leitor = leitorarquivo('data.txt')
    valores = leitor.getValores()
    print(valores)


main()

