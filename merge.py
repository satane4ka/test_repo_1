# Сортировка пузырьком
def merge(left : list, right : list) -> list:  # Функция слияния
    answer = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
    
    while i < len(left):
        answer.append(left[i])
        i += 1
        
        
    while j < len(right):
        answer.append(right[j])
        j += 1

    return answer


def merge_sort(arr : list) -> list:  # Функция разделения массива
    if len(arr) <= 1 or len(arr) == 2 and arr[0] <= arr[1]:
            return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    answer = merge(left_half, right_half)
    
    return answer

