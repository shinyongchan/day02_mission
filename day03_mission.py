#ch6-ex3

guess_me = 5
number = 1
for number in range(1,10) :
    if  guess_me>=number :
        print('too low')
    if guess_me==number :
        print('found it!')

else :
    print ('oops')

