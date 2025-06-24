def bubble_sort(array):
    for i in range(n:=len(array)):
        for j in range(0, n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]

    return array


array = [34,343,98, 12]
print(bubble_sort(array))

