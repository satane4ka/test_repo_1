import time
from bouble import bouble_sort
from merge import merge_sort


def time_counter_bouble(arr : list):
    start = time.perf_counter()

    sorted_arr = bouble_sort(arr)

    finish = time.perf_counter()

    answer = finish - start

    return f'Время сортировки пузырьком: {answer}'


def time_counter_merge(arr : list):
    start = time.perf_counter()

    sorted_arr = merge_sort(arr)

    finish = time.perf_counter()

    answer = finish - start

    return f'Время сортировки слиянием: {answer}'
    