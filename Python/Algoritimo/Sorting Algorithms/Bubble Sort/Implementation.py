# lista = [5616,51,651,65,6,68]

def sort_by_descending(list_of_numbers):
    for j in range(len(list_of_numbers) - 1):
        for i in range(len(list_of_numbers) - 1 - j):
            if list_of_numbers[i] < list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]


def sort_by_ascending(list_of_numbers):
    for j in range(len(list_of_numbers) - 1):
        for i in range(len(list_of_numbers) - 1 - j):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]


# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
