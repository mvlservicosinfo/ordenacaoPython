class Ordenacao_func:

    __lista = []
    def __init__(self, lista):
        self.lista = lista


#Bubbe Sort
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        print(f"Troca:{lista}")
        print(f"Passada: {i+1}: {lista}")
        return lista

#Insert Sort
    def insert_sort(lista):
        #comeca do segundo (indice 1 ) e vai o ultimo elemento
        for i in range(1, len(lista)):
            chave = lista[i] # Guarda o elemento atual
            j = i - 1 # O indice do elemnto anterior
    #move os elementos da lista que são maiores que a chave para uma posição
    #a frente da sua posição atual
            while j >= 0 and chave < lista[j]:
                lista[j+1] = lista[j]
                j -= 1
                print(f"Movimentação: {lista}")
      #coloca a chave na posição correta
            lista[j+1] = chave
            print(f"Inserção: {i}: {lista}")
        return lista


#Selection Sort

    def selection_sort(lista):
        for i in range(len(lista)):
            min = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[min]:
                    min = j
                #Troca o menor elemento encotrado com o primeiro
                    lista[i], lista[min] = lista[min], lista[i]
                    print(f"Troca: {i+1}: {lista}")
        return lista

# Merge Sort

    # Merge Sort

    def merge_sort(lista):
        # Verificar se a lista tem mais de um elemento
        if len(lista) > 1:
            # Dividir a lista em duas metades
            meio = len(lista) // 2
            esquerda = lista[:meio]
            direita = lista[meio:]
            # Recursivamente ordenar a primeria metade
            merge_sort(esquerda)
            # Recursivamente ordenar a segunda metade
            merge_sort(direita)
            # Inicializar os índices para percorrer as duas metades
            i = j = k = 0
            # Copiar os elementos ordenados de volta para a lista original
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    lista[k] = esquerda[i]
                    i += 1
                else:
                    lista[k] = direita[j]
                    j += 1
                k += 1

                # Verificar se resta elemento na metade esquerda
                while i < len(esquerda):
                    lista[k] = esquerda[i]
                    i += 1
                    k += 1
            # Verificar se resta elemento na metade direita
            while j < len(direita):
                lista[k] = direita[j]
                j += 1
                k += 1
                print(f"Merge: {lista}")
        return lista

    import random
    lista_exemplo = random.sample(range(100), 10)
    print("Lista Original")
    print(lista_exemplo)
    print("\nOrdenando...\n")
    lista_ordenada = merge_sort(lista_exemplo)
    print("\nLista Ordenada:")
    print(lista_ordenada)

#Quick sort
def quick_sort(lista):
  #Funcao Auxiliar para realizar a prticao
  def particao(lista, baixo, alto):
    #Pivo e o ultimo elemento
    pivo = lista[alto]
    i = baixo - 1
    #Percorre a lista do indice do menor elemento
    #até o indice do pivo
    for j in range(baixo, alto):
      if lista[j] <= pivo:
        i += 1
        #troca os elementos
        lista[i], lista[j] = lista[j], lista[i]
        #troca o pivo para posicao correta
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

  #Funcao Recursiva principal do quick sort
  def quick_sort_recursiva(lista, baixo, alto):
      if baixo < alto:
        #Indice da Particao
        p = particao(lista, baixo, alto)
        #Ordena os elementos antes e depois da particao
        quick_sort_recursiva(lista, baixo, p - 1)
        quick_sort_recursiva(lista, p + 1, alto)
  #Chamada inicial da funcao recursiva
  quick_sort_recursiva(lista, 0, len(lista) - 1)
  return lista

import random

lista_exemplo= random.sample(range(100), 10)
print("Lista Original")
print(lista_exemplo)
print("\nOrdenando...\n")
lista_ordenada = quick_sort(lista_exemplo)
print("\nLista Ordenada:")
print(lista_ordenada)

#Shell sort

def shell_sort(lista):
  n = len(lista)
  intervalo = n // 2
  #Dividindo o intervalo ate que saja igual a Zero
  while intervalo > 0:
    #Percorre a lista
    for i in range(intervalo, n):
      temp = lista[i]
      j = i
      while j >= intervalo and lista[j - intervalo] > temp:
        lista[j] = lista[j - intervalo]
        j -= intervalo
        #inserir o valor guardado na posicao correta
        lista[j] = temp
        #exibir a lista apos cada reducao de intervalo
    print(f"Intervalo {intervalo} : {lista}")
    intervalo //= 2
  return lista

import random

lista_exemplo= random.sample(range(100), 10)
print("Lista Original")
print(lista_exemplo)
print("\nOrdenando...\n")
lista_ordenada = shell_sort(lista_exemplo)
print("\nLista Ordenada:")
print(lista_ordenada)

