#05
import random
secret = random.randint(1,10) # 1에서 10 사이의 정수가 임의로 발생
guess = int(input('1~10사이의 수 :'))
if guess>secret :
    print('too high')
else :
    if guess==secret :
        print('just right')
    else :
        print('too low')


