class Contagem:
    def __init__(self, conjunto_dados):
        self.conjunto_dados = conjunto_dados

    def contar(self):
        primeiro = self.conjunto_dados[0]
        ultimo = self.conjunto_dados[-1]
        valores_inteiros = [x for x in range(primeiro, ultimo + 1) if isinstance(x, int)]
        return len(valores_inteiros)

# Na pratica
dados = [5, 67, 24, 74, 12]
contagem = Contagem(dados)
n_valores_inteiros = contagem.contar()
print("Quantidade de valores inteiros entre o primeiro dado e o último dado:", n_valores_inteiros)
