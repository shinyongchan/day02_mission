#Ch11_1
def score_sort(ary):
    for end in range(1, len(ary)):
        for i in range(end, 0, -1):
            if ary[i][1] < ary[i-1][1]:
                ary[i], ary[i-1] = ary[i-1], ary[i]
    return ary

score_ary = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]
print("정렬전 ---> ", score_ary)
score_sort(score_ary)
print("정렬후 ---> ", score_ary)
print("성적별 조 편성표")
for i in range (len(score_ary)//2):
    print(f'{score_ary[i][0]} : {score_ary[len(score_ary)-1-i][0]}')