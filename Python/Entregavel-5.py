class Quicksort:
    def tamanho_array(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            menores = [x for x in array[1:] if x <= pivot]
            maiores = [x for x in array[1:] if x > pivot]
            return self.tamanho_array(menores) + [pivot] + self.tamanho_array(maiores)

# Na pratica
array = [8, 10, 21, 48, 93, 11, 62]
print("Array não ordenado:", array)

chamando_quicksort = Quicksort()
array_ordenado = chamando_quicksort.tamanho_array(array)

print("Array ordenado:", array_ordenado)
