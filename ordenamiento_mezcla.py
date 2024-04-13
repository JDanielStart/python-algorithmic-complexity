import random

# 0(n log n) due to halving the list in each recursive call
def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Recursive call in each half
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Iterators to traverse the two sublists
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(izquierda) and j < len(derecha): # 0(n)
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda): # 0(n)
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha): # 0(n)
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(f'Lista sin ordenar: {lista} \n')

    lista_ordenada = ordenamiento_mezcla(lista)
    print(f'Lista ordenada: {lista_ordenada}')