# Without min or max function

def sort_by_ascending(lista):
    for i in range(len(lista) - 1):  # -1 because the last element will already be the last

        min_value = lista[i]

        for j in range(i + 1, len(lista)):
            if min_value > lista[j]:
                min_value = lista[j]

        min_index = lista.index(min_value,
                                i)  # Start the index search from the i position ( to work for duplicate order )
        if lista[i] != lista[min_index]:  # If the min its already in its position then do nothing otherwise ...
            lista[i], lista[min_index] = lista[min_index], lista[i]

    print(lista)


def sort_by_descending(lista):
    for i in range(len(lista) - 1):  # -1 because the last element will already be the last

        max_value = lista[i]

        for j in range(i + 1, len(lista)):
            if max_value < lista[j]:
                max_value = lista[j]

        max_index = lista.index(max_value,
                                i)  # Start the index search from the i position ( to work for duplicate order )
        if lista[i] != lista[max_index]:  # If the min its already in its position then do nothing otherwise ...
            lista[i], lista[max_index] = lista[max_index], lista[i]

    print(lista)


sort_by_ascending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])
sort_by_descending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])



