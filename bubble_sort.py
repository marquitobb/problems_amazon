
def bubbleSort(array):
    length = len(array) -1

    # TODO: optimeze this
    for _ in range(0, length):
        for j in range(0, length):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

scores = [23, 45, 12, 89, 32, 76, 18, 43, 56, 87]
print("Before sorting: ", scores)
print("After sorting: ", bubbleSort(scores))