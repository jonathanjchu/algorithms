def selection_sort(arr):
    print(arr)
    for i in range(len(arr)):
        minIdx = i
        
        for j in range(i, len(arr)):
            if  arr[j] < arr[minIdx]:
                minIdx = j
        
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

        print(arr)


test = [7, 2, 4, 1, 3, 20, -2, 5, 29, -42, 58, 67, 19, 430, 85, -31]

selection_sort(test)

print(test)