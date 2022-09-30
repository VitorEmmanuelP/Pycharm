def binary_search(list_of_numbers,key):

    low = 0
    high = len(list_of_numbers) - 1

    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if key == list_of_numbers[mid]:
            found = True
        elif key > list_of_numbers[mid]:
            low = mid + 1
        else:
            high = mid + 1

    if found:
        print('Key is found')
    else:
        print('Key not in the list')


lista = [23,1,4,2,3]
lista.sort()

key = int(input('Enter the key: '))

binary_search(lista,key)
