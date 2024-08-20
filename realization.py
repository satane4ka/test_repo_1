from counter import time_counter_bouble, time_counter_merge
from random import randint


# Создание массива
def arr_maker(arr : list) -> list:
    for i in range(1001):
        new_num = randint(1, 10000)
        arr.append(new_num)
    return arr


def main():
    nums = []
    
    new_arr = arr_maker(nums)
    
    b_result = time_counter_bouble(new_arr)
    m_result = time_counter_merge(new_arr)
    
    print(b_result, m_result, sep='\n')