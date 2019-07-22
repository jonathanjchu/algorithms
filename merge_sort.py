
def merge_sort(arr):
    print(arr)

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    print(f"merging {left} with {right}")

    output = []

    il = 0
    ir = 0
    while (il < len(left) or ir < len(right)):
        if il == len(left):
            output.append(right[ir])
            ir += 1
        elif ir == len(right):
            output.append(left[il])
            il += 1
        elif left[il] < right[ir]:
            output.append(left[il])
            il += 1
        else:
            output.append(right[ir])
            ir += 1

    print(f"result: {output}")
    return output




testArr = [56, 39, -4, 18, 108, 115, -6, 104, 67, 30, 98, 117, -17, 25, -53, 84, 76, 120, -57, 135]
testArr2 = [-71, -57, 150, 69, 135, 64, -47, 74, 70, -76, 71, 90, 73, -30, -49, 108, 109, 12, -59, 21, 13, -43, 4, -13, 102, -58, -92, -79, -3, -17, -40, 92, -5, 119, 122, 53, -29, -31, 50, -96, 34, -95, -46, 72, -78, 136, -27, 101, -93, -60]
merge_sort(testArr2)