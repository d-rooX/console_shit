import random as r
from clear import clear
from tabulate import tabulate
from tables import *
from words import adjectives_c, nouns_c

class City:
    def __init__(self):
        self.name = f"{r.choice(adjectives_c).title()} {r.choice(nouns_c)}"

    class Shop:
        def __init__(self):
            # 5 low, 4 medium и 2 high. Так я сделал для того, чтобы сделать больший шанс для выпадения маленькой экономики и меньший для большой
            self.economics = r.choice(("low", "low", "low", "low", "low", "medium", "medium", "medium", "medium", "high", "high"))

            # low - 0:2, medium - 3:4, high - 5:6
            self.amount = r.randint(0, 2) if self.economics == "low" else r.randint(3,4) if self.economics == "medium" else r.randint(5,6)
            # разница рыночной цены (цены в словаре) от цены в этом городе
            self.diff = r.randint(-15, -4) if self.economics == "low" else r.randint(-3,15) if self.economics == "medium" else r.randint(15, 30)

            # random.sample(population, k) - список длиной k из последовательности population.
            self.assortment = [get_item(id, self.diff) for id in r.sample(get_all_ids(), self.amount)]


        def check(self):
            tbl_headers = ["Предмет", "Характеристики", "Тип", "Цена"]
            tbl_objects = []
            for shop_item in self.assortment:
                tbl_objects.append([shop_item["name"], f'+{shop_item["pwr"]} {items_ends[shop_item["type"]]}',
                                    types_table[shop_item["type"]], shop_item["price"]])
            # В зависимости от типа экономики выбираем оформление таблицы
            tablefmt = "simple" if self.economics == "low" else "grid" if self.economics == "medium" else "fancy_grid"
            print(tabulate(tbl_objects, headers=tbl_headers, tablefmt=tablefmt))

    shop = Shop()

class NPC:
    def __init__(self, name, hp, attack, defend, lvl):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defend = defend
        self.lvl = lvl

class Player:
    class Inventory:
        def __init__(self, size=3):
            self.inv = []
            self.size = size

        def add(self, item):
            if len(self.inv) < self.size:
                item.update({"is_equipped":False})
                self.inv.append(item)
                print(f'Обьект "{item["name"]}" добавлен в инвентарь')
            else:
                print("Инвентарь переполнен")


        def check(self):
            if len(self.inv) > 0:
                tbl_headers = ["Предмет", "Характеристики", "Тип", "Экипирован?"]
                tbl_objects = []
                for item in self.inv:
                    tbl_objects.append([item["name"], f'+{item["pwr"]} {items_ends[item["type"]]}', types_table[item["type"]], "Да" if item["is_equipped"] else "Нет"])
                print(tabulate(tbl_objects, headers=tbl_headers, tablefmt="grid"))
            else:
                print("Твой инвентарь пуст...")

    inventory = Inventory()

    def __init__(self, name, maxhp = 10, lvl = 0):
        self.name = name
        self.money = 0

        # Максимально возможное ХП перса
        # ХП перса изначально равно максимальному
        self.hp = maxhp
        self.maxhp = maxhp

        self.lvl = lvl
        self.xp = 0
        self.needXP = xp_table[lvl]

        self.attack = 1
        self.defend = 1

        self.sword = None
        self.shield = None

        self.shop_available = False
        self.fight_available = False

    def fight(self, npc):
        if self.fight_available:
            print(f'Вы атаковали {npc.name}')
            table = [["", "Уровень", "Здоровье", "Атака", "Защита"],
                    [self.name, self.lvl, self.hp, self.attack, self.defend],
                    [npc.name, npc.lvl, npc.hp, npc.attack, npc.defend]]
            print(tabulate(table, headers="firstrow"))
            print("Провести бой автоматически?")
            inp = input("Напишите \"да\" или нажмите Enter для отказа")
            if inp == "да" or inp == "Да":
                auto = True
            else:
                auto = False
            while True:
                # чистим консоль
                clear()

                # Проверяем здоровье. Получаем уровень при победе
                if self.hp <= 0:
                    print(f'Ты проиграл этот бой')
                    break
                elif npc.hp <= 0:
                    ends = ('обезглавлен!', 'беспощадно убит!', 'теперь не вернётся домой...', 'пожалел о вашей встрече...')
                    print(f'{npc.name} {r.choice(ends)}')
                    self.get_xp(xp_table[npc.lvl])
                    break
                else:
                    # Рандом определяет кто сколько урона получит, учитывая уровень защиты
                    pl_dmg = r.randint(0, npc.attack) - r.randint(0, self.defend)
                    npc_dmg = r.randint(0, self.attack) - r.randint(0, npc.defend)

                    # Учитываем контратаку (отрицательный урон), и обнуляем урон если таковая случилась
                    if pl_dmg < 0: npc_dmg -= pl_dmg; pl_dmg = 0
                    if npc_dmg < 0: pl_dmg -= npc_dmg; npc_dmg = 0
                    # -1 урон это контратака. Соответственно если ты получил -1 урона, твоя защита сыграла на руку и ты дал
                    # внеплановых пиздюлей. Или же наоборот, если враг получил -1 урона, то у него свершилось тоже самое и
                    # потому лови свою плюху

                    # Отнимаем урон от ХП
                    self.hp -= pl_dmg
                    npc.hp -= npc_dmg

                    # В зависимости от полученого урона, выводим соответсвующее сообщение...
                    if not auto:
                        if pl_dmg == 0 and npc_dmg == 0:
                            print("Постояли подумали...")
                        elif pl_dmg == 0 and npc_dmg > 0:
                            print(f'Ты нанёс {npc_dmg} урона')
                        elif pl_dmg > 0 and npc_dmg == 0:
                            print(f'Ты получил {pl_dmg} урона')
                        else:
                            print(f'Ты получил {pl_dmg} урона, а нанёс {npc_dmg}')
                        print(tabulate([["Имя", "HP"], [self.name, self.hp], [npc.name, npc.hp]], headers = "firstrow"))
                        input("Enter...")
        else:
            print("Некого атаковать...")

    def get_xp(self, xp):
        self.xp += xp
        if self.xp >= self.needXP:
            # тк уровень может повыситься за один раз не только на 1, мы делаем цикл
            while self.xp >= self.needXP:
                # Добавляем уровень
                self.lvl += 1
                # Считаем разницу опыта и того который нужен для след. уровня, а потом меняем нужное количество опыта исходя из таблицы
                self.xp -= self.needXP
                self.needXP = xp_table[self.lvl]
            print(
                f'Ты повысил свой уровень до {self.lvl}, теперь у тебя {self.xp} опыта, и нужно набрать ещё {self.needXP - self.xp}')
        else:
            print(f'Ты получил {xp} XP')

    def get_money(self, money):
        self.money += money
        print(f'Ты получил {money} биткоинов')

    def spend_money(self, money):
        self.money -= money
        print(f'Ты потратил {money} биткоинов')

    def buy(self, shop, item_index, inventory = inventory):
        assortment = shop.assortment
        if shop.amount > 0 and assortment[item_index] and assortment[item_index]["price"] <= self.money:
            inventory.add(shop.assortment[item_index])
            self.spend_money(assortment[item_index]["price"])
        else:
            print("Ты не можешь купить эту вещь")

    def equip(self, item_index, inv = inventory.inv):
        try:
            item = inv[item_index]
            if self.sword != item["id"] and self.shield != item["id"]:
                if item["type"] == "sword":
                    self.sword = item["id"]
                    self.attack = item["pwr"]+1
                    inv[item_index]["is_equipped"] = True
                    print(f'Вы взяли в руки меч {item["name"]}')
                elif item["type"] == "shield":
                    self.shield = item["id"]
                    self.defend = item["pwr"]+1
                    inv[item_index]["is_equipped"] = True
                    print(f'Вы взяли в руки щит {item["name"]}')
        except:
            print("Не прикалывайся.")

    def get_stats(self):
        print(tabulate([["Деньги", "Опыт", "Уровень", "HP", "Атака", "Защита"],
                        [self.money, self.xp, self.lvl, self.hp, self.attack, self.defend]],
                       headers="firstrow", tablefmt="github"))
