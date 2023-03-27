def heapify(unsorted, heap_size, index):
    largest = index
    l = (2 * index) + 1  # ����
    r = (2 * index)  # �k��
    if l < heap_size and unsorted[index] < unsorted[l]:  # �p�G�{�b����o�Ӥ���j
        largest = l
    if r < heap_size and unsorted[largest] < unsorted[r]:  # �p�G�{�b�k��o�Ӥ���j
        largest = r  
    if largest != index:
        unsorted[index], unsorted[largest] = unsorted[largest], unsorted[index]
        heapify(unsorted, heap_size, largest)

def heap_sort(unsorted):
    n = len(unsorted)  # �}�C����
    for i in range(n // 2, -1, -1):  # ���U��
        heapify(unsorted, n, i)
    for i in range(n - 1, 0, -1):
            # Swap
        unsorted[i], unsorted[0] = unsorted[0], unsorted[i]
        heapify(unsorted, i, 0)


unsorted = [1, 4, 7, 2, 1, 3, 2, 5, 4, 2]
heap_sort(unsorted)
print("Sorted array : ")
for i in range(len(unsorted)):
    print("%d " % unsorted[i], end='')
