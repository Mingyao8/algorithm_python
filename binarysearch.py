import sys
def binary_search(data, key):
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) // 2  
        if data[mid] < key:   
            low = mid + 1
        elif data[mid] > key:
            upper = mid - 1
        else:                    
            return mid
    return -1

data = [1, 3, 5, 7, 9, 10]
for i in sys.stdin:
    i = int (i)
    index = binary_search(data, i)
    if index >= 0:
        print("at " + str(index))
    else:
        print("none")