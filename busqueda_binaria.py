import random

# O(log n) logaritmica
def busqueda_binaria(lista, comienzo, final, objetivo):
    if comienzo > final: # O(1)
        return False
    
    medio = (comienzo + final) // 2 # O(1)

    if lista[medio] == objetivo: # O(1)
        return True
    elif lista[medio] < objetivo: # O(1)
        return busqueda_binaria(lista, medio + 1, final, objetivo) # T(n) = T(n/2) + C
    else: # O(1)
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo) # T(n) = T(n/2) + C


if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamaño_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')