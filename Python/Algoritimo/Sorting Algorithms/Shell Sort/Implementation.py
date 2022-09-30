def shell_sort(list_of_numbers):

    gap = len(list_of_numbers) // 2

    while gap > 0:

        for index in range(gap, len(list_of_numbers)):

            concurrent_element = list_of_numbers[index]
            pos = index

            while pos >= gap and concurrent_element < list_of_numbers[pos - gap]:

                list_of_numbers[pos] = list_of_numbers[pos - gap]
                pos = pos - gap

            list_of_numbers[pos] = concurrent_element

        gap = gap // 2

    print(list_of_numbers)


lista = [20,50,4,89,7,36,1]

shell_sort(lista)
