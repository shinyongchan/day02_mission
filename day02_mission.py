import random

small = random.choice([True,False])
print (small)
green = random.choice([True,False])
print (green)


# small = True
# green = True

if small:
    if green:
        print('완두콩')
    else:
        print('체리')
else:
    if green:
        print('수박')
    else:
        print('호박')

