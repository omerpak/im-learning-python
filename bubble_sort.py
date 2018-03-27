def bubble_sort_algorithm(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    
    return array

myNumbers = [1, 36, 4, 5, 97, 1, 8, 35, 8, 8, 2, 17]

print("Sorted array: {}".format(bubble_sort_algorithm(myNumbers)))
