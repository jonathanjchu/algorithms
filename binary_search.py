def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    mid = right // 2
    count = 0

    while (right - left >= 0):
        count += 1
        print(f"index: {mid}")
        if val == arr[mid]:
            print(f"{val} found at index {mid} of array {arr}; {count} comparisons made")
            return mid
        elif val < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
        mid = left + (right - left) // 2
    
    print(f"{val} not found in array {arr}; {count} comparisons made")
    return None



arr = [-97, -94, -85, -84, -82, -69, -63, -62, -45, -38, -26, -25, -20, -16, -15, -13, -5, -4, 1, 11, 12, 19, 24, 37, 43, 50, 57, 72, 87, 100, 106, 146, 150, 161, 168, 169, 171, 172, 181, 183, 184, 192, 197, 202, 203, 206, 212, 214, 218, 222]
val = 11
binary_search(arr, val)
