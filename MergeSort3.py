def mergeSort(array):
    result = []
    if len(array) < 2:
        return array
    mid = int(len(array)/2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
    return result

nums = [3,5,7,12,2,6,9,23,1]
print(nums)
sort = mergeSort(nums)
print (sort)
