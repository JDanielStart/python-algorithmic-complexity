import random

# O(n) lineal
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # 0(n)
        if elemento == objetivo: # 0(1)
            match = True
            break

    return match


if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')