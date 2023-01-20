#ch10_ex 10.7

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'({self.name}, {self.symbol}, {self.number})'


hydrogen = Element('Hydrogen', 'H', '1')
print(hydrogen)



