xp_table = {0: 10, 1: 20, 2: 30, 3: 50, 4: 100, 5: 200, 6: 350, 7: 500, 8: 1000, 9: 3500, 10: 5000}
hp_table = {0: 10, 1: 15, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}

npc_table = {
        0: {"name": "Пидормотский жукотрёп", "lvl": 0, "attack": 1, "defend": 1},
        1: {"name": "Вьющийся гнездун", "lvl": 1, "attack": 2, "defend": 1},
        2: {"name": "Мохнатый писькогрыз", "lvl": 2, "attack": 2, "defend": 2},
        3: {"name": "Какой-то еблозавр", "lvl": 3, "attack": 3, "defend": 2},
        4: {"name": "Жопоногий членорук", "lvl": 4, "attack": 4, "defend": 3},
        5: {"name": "Супербыстрый сопель", "lvl": 5, "attack": 4, "defend": 4},
        6: {"name": "Чебурирубщий бульдоратор", "lvl": 6, "attack": 5, "defend": 5},
        7: {"name": "Подретузный запах", "lvl": 7, "attack": 6, "defend": 5},
        8: {"name": "Лютый дудец", "lvl": 8, "attack": 7, "defend": 7},
}

items_ends = {"sword": "к максимальному урону", "shield": "к максимальной защите", "heal": "к текущему здоровью"}
types_table = {
        "sword":  "Меч",
        "shield": "Щит",
        "heal":   "Хилка",
}

items_table = {
        "sword":  {
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
        "item":   {
                "hl1": {"name": "Тухлый чифир", "pwr": 3, "price": 15, "type": "heal", "id": "hl1"},
                "hl2": {"name": "Бабушкин навар", "pwr": 5, "price": 20, "type": "heal", "id": "hl2"},
                "hl3": {"name": "Едрёный шлак", "pwr": 8, "price": 30, "type": "heal", "id": "hl3"},
                "hl4": {"name": "Лютое пойло", "pwr": 10, "price": 50, "type": "heal", "id": "hl4"},
        }
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
