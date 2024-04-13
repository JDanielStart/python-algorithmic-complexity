import random

# O(n^2) quadratic very inefficient for large data sets
def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n): # O(n)
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n^2)

            if lista[j] > lista[j + 1]: # O(1)
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # O(1)

    return lista

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(f'Lista sin ordenar: {lista} \n')

    lista_ordenada = ordenamiento_burbuja(lista)
    print(f'Lista ordenada: {lista_ordenada}')