if __name__ == '__main__':
 pass
import random
lista_exemplo= random.sample(range(100), 10)
print("Lista Original")
print(lista_exemplo)
print("\nOrdenando...\n")
lista_ordenada = bubble_sort(lista_exemplo)
print("\nLista Ordenada:")
print(lista_ordenada)