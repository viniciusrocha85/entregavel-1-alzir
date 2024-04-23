class Somatorio:
    def __init__(self, numeros):
        self.numeros = numeros

    def calcular_somatorio(self):
        return sum(self.numeros)

# Na pratica
numeros = [1, 5, 10, 20, 40]
somatorio = Somatorio(numeros)
resultado = somatorio.calcular_somatorio()
print("O somatório dos números é:", resultado)
