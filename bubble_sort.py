
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            print(arr)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            


testArr = [-84, 133, 41, 132, 137, 33, 62, 163, 6, 115, 16, 177, -64, 55, -51, -99, -56, -77, -80, -52, 85]
bubble_sort(testArr)
print(testArr)