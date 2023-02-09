#Ch12_2
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




data_ary = [random.randint(0,800000) for _ in range(100000)]
rand = random.randint(0, len(data_ary)-1)
data_ary.sort()
data_ary.insert(rand, data_ary[50])
start = time.time()
quick_sort(data_ary, 0, len(data_ary)-1)
end = time.time()

print(f'데이터 수 : {100000} 개')
print(f'끼어든 위치 : {rand}')
print(f'퀵 정렬 : {end - start}초')



