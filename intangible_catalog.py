import random

INTANGIBLE_TITLES_LIST = [
    "Рефакторинг модуля загрузки",
    "Рефакторинг запросов к БД",
    "Рефакторинг аутентификации",
    "Рефакторинг публичного API",
    "Рефакторинг бизнес-процесса",
    "Рефакторинг GUI",
    "Рефакторинг модуля выгрузки",
    "Обновить версию Postgres",
    "Обновить версию React",
    "Обновить docker",
    "Обновить redis",
    "Обновить ОС на виртуалках",
    "Обновить JAVA",
    "Задокументировать код",
    "Провалидировать автотесты"
]

gen = (i for i in INTANGIBLE_TITLES_LIST)


def get_random_title():
    return INTANGIBLE_TITLES_LIST[random.randrange(0, INTANGIBLE_TITLES_LIST.__len__())]
