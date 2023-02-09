#Ch11_2
def ary_sort(ary):
    for end in range(1, len(ary)):
        for i in range(end, 0, -1):
            if ary[i] < ary[i-1]:
                ary[i], ary[i-1] = ary[i-1], ary[i]
    return ary

ary2 = [[55, 33, 250, 44], [88,  1,  67, 23], [199,222, 38, 47], [155,145, 20, 99]]
ary1 = []

for i in range(len(ary2)):
    ary1 = ary1 + ary2[i]
print("1차원 변경 후, 정렬 전 : ", ary1)
print("1차원 변경 후, 정렬 후 : ", ary_sort(ary1))
print("중앙값 : ", ary1[len(ary1)//2])