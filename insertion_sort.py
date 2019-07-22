def insertion_sort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print(arr)

test = [2, -5, 28, 60, 3, 58, 201, 24, -10, 80, -98, 75, 32, 198, -53, 22]
insertion_sort(test)
print(test)
