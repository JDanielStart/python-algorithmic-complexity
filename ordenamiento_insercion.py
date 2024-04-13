import random

# 0(n^2) quadratic very inefficient for large data sets
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)): # O(n)
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual: # O(n) * O(n) = O(n^2)
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(f'Lista sin ordenar: {lista} \n')

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(f'Lista ordenada: {lista_ordenada}')