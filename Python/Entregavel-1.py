class Numeroprimo:
    def __init__(self, numero):
        self.numero = numero

    def verificar_primo(self):
        if self.numero <= 1:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

#na pratica
num = int(input("Digite um número inteiro positivo: "))
primo = Numeroprimo(num)
if primo.verificar_primo():
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
