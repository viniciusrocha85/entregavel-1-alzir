class MDC:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular_mdc(self):
        while self.numero2 != 0:
            self.numero1, self.numero2 = self.numero2, self.numero1 % self.numero2
        return self.numero1

# na Pratica
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
mdc_calculadora = MDC(a, b)
mdc = mdc_calculadora.calcular_mdc()
print("O MDC de", a, "e", b, "é:", mdc)
