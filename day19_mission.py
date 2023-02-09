#Ch10_1
def notation(base, num):
    if base > num :
        print(number_char[num], end='')
    else:
        notation(base, num//base)
        print(number_char[num%base],end='')

number_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_char = number_char + ['A', 'B', 'C', 'D', 'E', 'F']
num = int(input("10진수 입력 : "))
print("2진수 : ", end='')
notation(2, num)
print()
print("8진수 : ", end='')
notation(8, num)
print()
print("16진수 : ", end='')
notation(16, num)
