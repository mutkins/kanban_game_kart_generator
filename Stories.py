import random
import math


def get_random_estimates(type='story'):
    start = 1
    stop = 10
    step = 2
    base_complexity = random.randrange(start=start, stop=stop, step=step) / 10

    if type == 'story':
        match base_complexity:
            case _ if base_complexity > (start + stop - 1)/10 / 5 * 4:
                price = 150
            case _ if base_complexity > (start + stop - 1)/10 / 5 * 3:
                price = 120
            case _ if base_complexity > (start + stop - 1)/10 / 5 * 2:
                price = 100
            case _ if base_complexity > (start + stop - 1)/10 / 5:
                price = 80
            case _:
                price = 60
    elif type == 'expedite':
        match base_complexity:
            case _ if base_complexity > 0.5:
                price = 3000
            case _:
                price = 2000
        price = price * -1 if random.randrange(2) > 0 else price

    match base_complexity:
        case _ if base_complexity > (start + stop - 1) / 10 / 5 * 4:
            stability_score = 5
        case _ if base_complexity > (start + stop - 1) / 10 / 5 * 3:
            stability_score = 4
        case _ if base_complexity > (start + stop - 1) / 10 / 5 * 2:
            stability_score = 3
        case _ if base_complexity > (start + stop - 1) / 10 / 5:
            stability_score = 2
        case _:
            stability_score = 1

    dev_estimate = math.floor(4 + base_complexity * 10)
    analyst_estimate = math.floor(dev_estimate / 2.5 + random.randrange(0, 5))
    test_estimate = math.floor(dev_estimate / 2.5 + random.randrange(0, 5))

    return {'price': price, 'analyst_estimate': analyst_estimate, 'dev_estimate': dev_estimate,
            'test_estimate': test_estimate, 'stability_score': stability_score}


class Stories:
    def __init__(self):
        self.stories_list = []

    def generate_u_stories(self, count, letter_index='S'):
        stories = []
        for i in range(count):
            estimate = get_random_estimates()
            stories.append(UsualStory(num=i, letter_index=letter_index, price=estimate['price'],
                                      analyst_estimate=estimate['analyst_estimate'],
                                      dev_estimate=estimate['dev_estimate'], test_estimate=estimate['test_estimate']))
        self.stories_list.append(stories)

    def generate_f_stories(self, count, letter_index='F'):
        stories = []
        j = 9
        for i in range(count):
            due_day = j + 4 + random.randrange(0, 3)
            j += 5
            estimate = get_random_estimates()
            stories.append(FixedDateStory(num=i, letter_index=letter_index, price=estimate['price'],
                                          analyst_estimate=estimate['analyst_estimate'],
                                          dev_estimate=estimate['dev_estimate'],
                                          test_estimate=estimate['test_estimate'], due_day=due_day))
        self.stories_list.append(stories)

    def generate_o_stories(self, count, letter_index='O'):
        stories = []
        for i in range(count):
            estimate = get_random_estimates()
            stories.append(OptimizationStory(num=i, letter_index=letter_index,
                                             analyst_estimate=estimate['analyst_estimate'],
                                             dev_estimate=estimate['dev_estimate'],
                                             test_estimate=estimate['test_estimate'], stability_score=estimate['stability_score']))
        self.stories_list.append(stories)

    def generate_e_stories(self, count, letter_index='E'):
        stories = []
        for i in range(count):
            due_day = random.randrange(3, 5)
            estimate = get_random_estimates(type='expedite')
            stories.append(ExpediteStory(num=i, letter_index=letter_index, price=estimate['price'],
                                         analyst_estimate=estimate['analyst_estimate'],
                                         dev_estimate=estimate['dev_estimate'],
                                         test_estimate=estimate['test_estimate'], due_day=due_day))
        self.stories_list.append(stories)


class Story:
    def __init__(self, num, letter_index, price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', color='green'):
        self.num = num
        self.letter_index = letter_index
        self.price = price
        self.analyst_estimate = analyst_estimate
        self.dev_estimate = dev_estimate
        self.test_estimate = test_estimate
        self.date_created = date_created
        self.color = color


class UsualStory(Story):
    def __init__(self, num, letter_index='S', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', color='green'):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate,
                         test_estimate=test_estimate, date_created=date_created, color=color, num=num)


class FixedDateStory(Story):
    def __init__(self, num, letter_index='F', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', due_day='1976-01-01', color='green'):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate, test_estimate=test_estimate, date_created=date_created,
                         color=color, num=num)
        self.due_day = due_day


class OptimizationStory(Story):
    def __init__(self, num, letter_index='O', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', color='green', stability_score=0):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate, test_estimate=test_estimate, date_created=date_created, color=color,
                         num=num)
        self.stability_score = stability_score


class ExpediteStory(Story):
    def __init__(self, num, letter_index='E', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', due_day='1976-01-01', color='green'):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate, test_estimate=test_estimate, date_created=date_created, color=color,
                         num=num)
        self.due_day = due_day
