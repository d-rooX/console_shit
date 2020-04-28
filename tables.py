xp_table = {0: 10, 1: 20, 2: 30, 3: 50, 4: 100, 5: 200, 6: 350, 7: 500}
ends = {"sw": "к максимальному урону", "sh": "к максимальной защите"}
types_table = {
    "sw": "Меч",
    "sh": "Щит",
    # "hl":"Хилка"
}
items_table = {
    "sword": {
        "sw1": {"name": "Ржавый еблоструй", "pwr": 1, "price": 10},
        "sw2": {"name": "Новый еблоструй", "pwr": 2, "price": 20},
        "sw3": {"name": "Тупой конец", "pwr": 3, "price": 30},
        "sw4": {"name": "Острый конец", "pwr": 4, "price": 40},
    },
    "shield": {
        "sh1": {"name": "Хлипкое моргало", "pwr": 1, "price": 10},
        "sh2": {"name": "Прочное моргало", "pwr": 2, "price": 20},
        "sh3": {"name": "Прикольный блокиратор", "pwr": 3, "price": 30},
        "sh4": {"name": "Хайповый блокиратор", "pwr": 4, "price": 40}
    },
    # "item": {
    #     "heal": {
    #         "Тухлый чифир": 2,
    #         "Бабушкин навар": 3,
    #         "Едрёный шлак": 4,
    #         "Лютое пойло": 10,
    #         "Кола с кофе": 9999
    #     }
    # }
}


def get_item(id):
    for type in items_table:
        for ids in items_table[type]:
            if id == ids:
                return items_table[type][id]


def get_item_type(id):
    for type in items_table:
        for ids in items_table[type]:
            if id == ids:
                return type


def get_all_ids():
    ids = []
    for type in items_table:
        for id in items_table[type]:
            ids.append(id)
    return ids
