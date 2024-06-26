import random


class InsertionSort:
    def __init__(self):
        pass

    lp = random.sample(range(100), 10)

    def insert_sort(self,lista=lp):

        # comeca do segundo (indice 1 ) e vai o ultimo elemento
        for i in range(1, len(lista)):
            chave = lista[i]  # Guarda o elemento atual
            j = i - 1  # O indice do elemnto anterior
            # move os elementos da lista que são maiores que a chave para uma posição
            # a frente da sua posição atual
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
                print(f"Movimentação: {lista}")
            # coloca a chave na posição correta
            lista[j + 1] = chave
        print(f"Inserção: {i}: {lista}")
        return lista





