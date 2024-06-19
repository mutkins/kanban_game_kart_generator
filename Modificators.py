from modificators_catalog import gen
class Modificators:
    def __init__(self):
        self.modificators_list = []

    def generate_modificators(self, count):
        troubles = []
        for i in range(count):
            troubles.append(Modificator(num=i, text=next(gen)))
        self.modificators_list.append(troubles)


class Modificator:
    def __init__(self, num, text=''):
        self.num = num
        self.text = text
        self.letter_index = 'M'
