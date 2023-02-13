#ch10_ex 10.9


class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(f'{bear.eats}, {rabbit.eats()}, {octothorpe.eats()}')







