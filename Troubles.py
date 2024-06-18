import random
from troubles_catalog import *
class Troubles:
    def __init__(self):
        self.troubles_list = []

    def generate_troubles(self, count, rate):
        troubles = []
        for i in range(count):
            match rate:
                case 0: text = next(harmless_gen)
                case 1: text = next(easy_gen)
                case 2: text = next(serious_gen)
                case 3: text = next(awful_gen)
            troubles.append(Trouble(num=i, price=get_random_price(rate), text=text, rate=rate))
        self.troubles_list.append(troubles)


class Trouble:
    def __init__(self, num, price=0, text='', rate=1):
        self.num = num
        self.price = price
        self.text = text
        self.rate = rate
        self.letter_index = 'T'


def get_random_price(rate):
    price = 0
    match rate:
        case 0: price = 0
        case 1: price = random.randrange(3, 6)
        case 2: price = random.randrange(6, 9)
        case 3: price = random.randrange(9, 12)
    return price




