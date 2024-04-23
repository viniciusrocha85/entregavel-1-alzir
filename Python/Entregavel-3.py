class Fibonacci:
    def __init__(self, numero):
        self.numero = numero

    def calcular_fibonacci(self):
        fibonacci = [0, 1]
        while len(fibonacci) < self.numero:
            novo_termo = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(novo_termo)
        return fibonacci

# Na pratica
quant_numeros = int(input("Digite o número de termos da sequência de Fibonacci que deseja calcular: "))
fibonacci_calculadora = Fibonacci(quant_numeros)
sequencia_fibonacci = fibonacci_calculadora.calcular_fibonacci()
print("Os primeiros", quant_numeros, "termos da sequência Fibonacci são:", sequencia_fibonacci)
