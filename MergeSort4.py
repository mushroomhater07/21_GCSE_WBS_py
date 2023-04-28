def mergeSort(array):
    result = []
    if len(array) < 2:
        return array
    mid = int(len(array)/2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0][1] > right[0][1]:
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

topFilms2017 = [['Beauty And The Beast','£72.4m'], ['Despicable Me 3','£47.8m'], ['Dunkirk','£56.6m'], ['Guardians Of The Galaxy Vol 2','£41m'], ['IT','£32.3m'], ['La La Land','£30.4m'], ['Paddington 2','£39.3m'], ['Spider-Man: Homecoming','£30.4m'], ['Star Wars: The Last Jedi','£73.1m'],['Thor: Ragnarok','£31m']]
sort = mergeSort(topFilms2017)
print(sort)
