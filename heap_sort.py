
def heap_sort(arr):
    
    def percolate_down(start, end):
        pos = start

        while (2 * pos + 1) <= end - 1:
            child = 2 * pos + 1

            # determine which child is larger
            if child + 1 <= end - 1 and arr[child] < arr[child + 1]:
                child += 1

            if arr[pos] < arr[child]:
                arr[pos], arr[child] = arr[child], arr[pos]
                pos = child
            else:
                return
    
    def heapify():
        # start at last parent
        start = (len(arr) - 1) // 2

        while start >= 0:
            percolate_down(start, len(arr))
            start -= 1


    heapify()

    print(f"heapified list: {arr}")
    print()
    print("sorting:")

    # actual sorting
    for i in range(len(arr) - 1, 0, -1):
        print(arr)
        arr[0], arr[i] = arr[i], arr[0]
        percolate_down(0, i)
  


testArr = [60, -37, 13, -64, 72, -39, 148, 65, 61, 126, 84, 132, 67, 1, 4, -13, -62, 26, 120, 28, -14, 43, -43, 79, 23, -61, 109, -8, -31, -34, -29, -94, 101, -72, 110, 82, 88, 136, -48, 66, 51, -4, 48, 54, 2, -59, -66, 90, -18, 139]
heap_sort(testArr)
print(testArr)


testArr2 = [63, -67, 83, -75, -18, 163, 207, 97, -35, -86, 190, 32, 104, 196, -49, -21, 96, 142, -72, 23, 187, 124, 135, 108, 10, 11, -13, 87, 31, -69, 143, -84, 209, 3, 131, 81, 21, 29, -89, 6, 125, 148, 211, -76, 205, 204, 130, 140, -30, 121]
heap_sort(testArr2)
print(testArr2)