def sort_by_descending(lista):
    for index in range(1, len(lista)):

        current_element = lista[index]
        pos = index

        while current_element > lista[pos-1] and pos > 0:
            lista[pos] = lista[pos - 1]
            pos -= 1

        lista[pos] = current_element

    print(lista)


def sort_by_ascending(lista):
    for index in range(1, len(lista)):

        current_element = lista[index]
        pos = index

        while current_element < lista[pos-1] and pos > 0:
            lista[pos] = lista[pos - 1]
            pos -= 1

        lista[pos] = current_element

    print(lista)


# lista = [2,4,3,5,1]

# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
