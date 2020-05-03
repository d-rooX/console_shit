xp_table = {0: 10, 1: 20, 2: 30, 3: 50, 4: 100, 5: 200, 6: 350, 7: 500, 8: 1000, 9: 3500, 10: 5000}
items_ends = {"sword": "к максимальному урону", "shield": "к максимальной защите"}
types_table = {
    "sword": "Меч",
    "shield": "Щит",
    # "hl":"Хилка"
}
items_table = {
    "sword": {
        "sw1": {"name": "Ржавый еблоструй", "pwr": 1, "price": 20, "type": "sword", "id": "sw1"},
        "sw2": {"name": "Новый еблоструй", "pwr": 2, "price": 35, "type": "sword", "id": "sw2"},
        "sw3": {"name": "Тупой конец", "pwr": 3, "price": 60, "type": "sword", "id": "sw3"},
        "sw4": {"name": "Острый конец", "pwr": 4, "price": 100, "type": "sword", "id": "sw4"},
    },
    "shield": {
        "sh1": {"name": "Хлипкое моргало", "pwr": 1, "price": 20, "type": "shield", "id": "sh1"},
        "sh2": {"name": "Прочное моргало", "pwr": 2, "price": 35, "type": "shield", "id": "sh2"},
        "sh3": {"name": "Прикольный блокиратор", "pwr": 3, "price": 60, "type": "shield", "id": "sh3"},
        "sh4": {"name": "Хайповый блокиратор", "pwr": 4, "price": 100, "type": "shield", "id": "sh4"}
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


def get_item(id, price_diff=0):
    for type in items_table:
        for ids in items_table[type]:
            if id == ids:
                res_item = items_table[type][id]
                res_item['price'] += price_diff
                return res_item


def get_all_ids():
    ids = []
    for type in items_table:
        for id in items_table[type]:
            ids.append(id)
    return ids
