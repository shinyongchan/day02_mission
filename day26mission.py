import random


def seq_search(ary, find_data):
    global count
    pos = -1
    for i in range(len(ary)):
        count = count +1
        if ary[i] == find_data:
            pos = i
            break
    return pos


def bin_search(ary, find_data):
    global count
    start = 0
    end = len(ary) - 1

    while start <= end:
        count = count +1
        mid = (start + end) // 2
        if find_data == ary[mid]:
            return mid
        elif find_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


count = 0
find_data = 6544
data_ary = [random.randint(0, 999999) for _ in range(1000000)]
data_ary.insert(random.randint(0, 1000000), find_data)
sorted_ary = sorted(data_ary)


pos = seq_search(data_ary, find_data)
if pos != -1:
    print(f'순차 검색(비정렬 데이터) : {count}회')
count = 0
pos = bin_search(sorted_ary, find_data)
if pos != -1:
    print(f'이진 검색(정렬 데이터) : {count}회')
