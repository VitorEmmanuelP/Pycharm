# lista = [5616,51,651,65,6,68]

def sort_by_descending(lista):
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1 - j):
            if lista[i] < lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]


def sort_by_ascending(lista):
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]


# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
