def sort_by_descending(list_of_numbers):
    for index in range(1, len(list_of_numbers)):

        current_element = list_of_numbers[index]
        pos = index

        while current_element > list_of_numbers[pos - 1] and pos > 0:
            list_of_numbers[pos] = list_of_numbers[pos - 1]
            pos -= 1

        list_of_numbers[pos] = current_element

    print(list_of_numbers)


def sort_by_ascending(list_of_numbers):
    for index in range(1, len(list_of_numbers)):

        current_element = list_of_numbers[index]
        pos = index

        while current_element < list_of_numbers[pos - 1] and pos > 0:
            list_of_numbers[pos] = list_of_numbers[pos - 1]
            pos -= 1

        list_of_numbers[pos] = current_element

    print(list_of_numbers)


# lista = [2,4,3,5,1]

# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
