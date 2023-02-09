#Ch12_1
import random
import time

def quick_sort(ary, start, end):
    if end <= start:
        return
    low = start
    high = end
    pivot = ary[(high + low) // 2]
    while low <= high:
        while ary[low] < pivot:
            low = low + 1
        while ary[high] > pivot:
            high = high - 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1

    mid = low
    quick_sort(ary, start, mid-1)
    quick_sort(ary, mid, end)


count_ary = [1000, 10000, 12000, 15000]
for i in count_ary:
    data_ary = [random.randint(0,800000) for _ in range(i)]
    start = time.time()
    quick_sort(data_ary, 0, len(data_ary)-1)
    end = time.time()
    print(f'데이터 수 : {i} 개')
    print(f'\t퀵 정렬 : {end - start}초')



