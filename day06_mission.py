#ch9_ex 9.3

def test_it (func) :
    def new_function (*args, **kwargs):
        print('start')
        print(func(*args, **kwargs))
        print('end')
    return new_function
@test_it
def add_ints(a,b) :
    return a+b
add_ints (3, 5)
