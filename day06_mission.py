#ch9_ex 9.4

class OopsException(Exception) :
    pass
words = ['eenie', 'meenie', 'miny', 'MO']
for word in words :
    if word.isupper() :
       try :
        raise OopsException
       except :
           print('Caught an oops')