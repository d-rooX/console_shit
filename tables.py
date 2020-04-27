xp_table = {0: 10, 1: 20, 2: 30, 3: 50, 4: 100, 5: 200, 6: 350, 7: 500}

types_table = {
    "sw":"Меч",
    "sh":"Щит",
    "hl":"Хилка"
}
items_table = {
    "sword": {
        "sw1": {"name": "Ржавый еблоструй", "pwr": 1},
        "sw2": {"name": "Новый еблоструй", "pwr": 2},
        "sw3": {"name": "Тупой конец", "pwr": 3},
        "sw4": {"name": "Острый конец", "pwr": 4},
    },
    "shield": {
        "sh1": {"name": "Хлипкое моргало", "pwr": 1},
        "sh2": {"name": "Прочное моргало", "pwr": 2},
        "sh3": {"name": "Прикольный блокиратор", "pwr": 3},
        "sh4": {"name": "Хайповый блокиратор", "pwr": 4}
    },
    "item": {
        "heal": {
            "Тухлый чифир": 2,
            "Бабушкин навар": 3,
            "Едрёный шлак": 4,
            "Лютое пойло": 10,
            "Кола с кофе": 9999
        }
    }
}


def get_item(id):
    for type in items_table:
        for ids in items_table[type]:
            if id == ids:
                return items_table[type][id]
