import random
import math


def get_random_estimates():
    base_complexity = random.randrange(start=1, stop=10, step=2) / 10
    price = int(50 + base_complexity * 50)
    dev_estimate = math.floor(4 + base_complexity * 10)
    analyst_estimate = math.floor(dev_estimate / 3 + base_complexity * 10)
    test_estimate = math.floor(dev_estimate / 3 + base_complexity * 10)
    return {'price': price, 'analyst_estimate': analyst_estimate, 'dev_estimate': dev_estimate,
            'test_estimate': test_estimate}


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
        for i in range(count):
            due_day = i + 9
            estimate = get_random_estimates()
            stories.append(FixedDateStory(num=i, letter_index=letter_index, price=estimate['price'],
                                          analyst_estimate=estimate['analyst_estimate'],
                                          dev_estimate=estimate['dev_estimate'],
                                          test_estimate=estimate['test_estimate'], due_day=due_day))
        self.stories_list.append(stories)

    def generate_i_stories(self, count, letter_index='I'):
        stories = []
        for i in range(count):
            due_day = i + 9
            estimate = get_random_estimates()
            stories.append(IntangibleStory(num=i, letter_index=letter_index, price=estimate['price'],
                                           analyst_estimate=estimate['analyst_estimate'],
                                           dev_estimate=estimate['dev_estimate'],
                                           test_estimate=estimate['test_estimate']))
        self.stories_list.append(stories)

    def generate_e_stories(self, count, letter_index='I'):
        stories = []
        for i in range(count):
            due_day = i + 9
            estimate = get_random_estimates()
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


class IntangibleStory(Story):
    def __init__(self, num, letter_index='I', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', color='green'):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate, test_estimate=test_estimate, date_created=date_created, color=color,
                         num=num)


class ExpediteStory(Story):
    def __init__(self, num, letter_index='E', price=0, analyst_estimate=0, dev_estimate=0, test_estimate=0,
                 date_created='1976-01-01', due_day='1976-01-01', color='green'):
        super().__init__(letter_index=letter_index, price=price, analyst_estimate=analyst_estimate,
                         dev_estimate=dev_estimate, test_estimate=test_estimate, date_created=date_created, color=color,
                         num=num)
        self.due_day = due_day
