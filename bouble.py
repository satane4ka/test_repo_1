# Сортировка пузырьком
def bouble_sort(arr : list) -> list:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            buf = 0
            if arr[i] > arr[j]:
                buf = arr[j]
                arr[j] = arr[i]
                arr[i] = buf
    
    return arr
