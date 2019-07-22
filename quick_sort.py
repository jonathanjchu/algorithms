
def quick_sort(arr):

    def quick_sort_helper(arr, start, end):
        if start < end:
            pivot = partition(arr, start, end)
            quick_sort_helper(arr, start, pivot)
            quick_sort_helper(arr, pivot+1, end)
        

    def partition(arr, start, end):
        temp1 = start
        temp2 = end + 1

        pivot = choose_pivot(arr, start, end)
        
        # print(f"start: {start}, end: {end}")
        print(f"pivot: {pivot}")
        print(f"sub array: {arr[start:end+1]}")

        while True:
            while arr[start] < pivot:
                start += 1
            
            while arr[end] > pivot:
                end -= 1
            
            if start >= end:
                print(f"paritioned sub array: {arr[temp1:temp2]}")
                return end
            
            arr[start], arr[end] = arr[end], arr[start]

            start += 1
            end -= 1

            print(arr[temp1:temp2])
        
    
    def choose_pivot(arr, start, end):
        mid = (start + end) // 2
        if arr[mid] < arr[start]:
            arr[start], arr[mid] = arr[mid], arr[start]
        if arr[end] < arr[start]:
            arr[start], arr[end] = arr[end], arr[start]
        if arr[mid] < arr[end]:
            arr[mid], arr[end] = arr[end], arr[mid]
        
        return arr[end]
        
    
    quick_sort_helper(arr, 0, len(arr)-1)


testArr = [0, 5, 15, -49, 21, 50, -23, 52, 63, -59, 222, 51, 96, 23, 80, 103, -5, 73]
testArr2 = [122, 146, 4, 37, -35, 112, 19, 2, 145, 70, 119, 87, -59, -89, -18, 44, -69, 53, 68, -55, -52, 93, 113, -82, -81, 81, -34, 20, 21, 23, 42, 101, -50, 80, -61, -68, -100, 1, -27, 26, 142, 32, 149, 132, -13, 3, 116, 73, -79, 67]
quick_sort(testArr2)
print(testArr)
