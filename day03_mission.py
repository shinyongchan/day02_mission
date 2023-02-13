number = int( input('정수를 입력 하시오 (1~10) : '))

for i in range(1,number*number+1) :
    if i % number==0 and i >= number:
        print(i)
        print('\n')
    else:
        print(i, end=' ')