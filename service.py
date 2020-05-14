import random as r
from clear import clear
from tabulate import tabulate
from tables import *
from words import *

class City:
    def __init__(self):
        self.generate()

    def generate(self):
        self.name = f"{r.choice(adjectives_c).title()} {r.choice(nouns_c)}"
        # 5 low, 4 medium и 2 high. Так я сделал для того, чтобы сделать больший шанс для выпадения маленькой экономики и меньший для большой
        self.economics = r.choice(("low", "low", "low", "low", "low", "medium", "medium", "medium", "medium", "high", "high"))

        # low - 0:2, medium - 3:4, high - 5:6
        self.amount = r.randint(0, 2) if self.economics == "low" else r.randint(3, 4) if self.economics == "medium" else r.randint(5, 6)
        # разница рыночной цены (цены в словаре) от цены в этом городе
        self.diff = r.randint(-15, -4) if self.economics == "low" else r.randint(-3, 15) if self.economics == "medium" else r.randint(15, 30)

        # random.sample(population, k) - список длиной k из последовательности population.
        self.assortment = [get_item(id, self.diff) for id in r.sample(get_all_ids(), self.amount)]

        # генерим отель или мотель в зависимости от экономики города
        self.hotel = True if self.economics == 'high' or self.economics == 'medium' else False
        self.hotel_cost = r.randint(20, 30) if self.economics == 'high' else r.randint(5, 10) if self.economics == 'medium' else 0
    def check_shop(self):
        tbl_headers = ["Предмет", "Характеристики", "Тип", "Цена"]
        tbl_objects = []
        for shop_item in self.assortment:
            tbl_objects.append([shop_item["name"], f'+{shop_item["pwr"]} {items_ends[shop_item["type"]]}',
                                types_table[shop_item["type"]], shop_item["price"]])
        # В зависимости от типа экономики выбираем оформление таблицы
        tablefmt = "simple" if self.economics == "low" else "grid" if self.economics == "medium" else "fancy_grid"
        print(tabulate(tbl_objects, headers=tbl_headers, tablefmt=tablefmt))
    def check_city(self):
        rows = (
            ['Название города', self.name],
            ['Уровень экономики', self.economics],
            ['Есть ли отель?', f'{"Да" if self.hotel else "Нет"}'],
            ['Разница цен', self.diff]
        )
        print(tabulate(rows))

class Player:
    class Inventory:
        def __init__(self, size=3):
            self.size = size
            self.inv = []

        def add(self, item):
            if len(self.inv) < self.size:
                item.update({"is_equipped": False}) if item["type"] in ("sword", "shield") else None
                self.inv.append(item)
                print(f'Обьект "{item["name"]}" добавлен в инвентарь')
            else:
                print("Инвентарь переполнен")
        def check(self):
            if len(self.inv) > 0:
                tbl_headers = ["Предмет", "Характеристики", "Тип", "Экипирован?"]
                tbl_objects = []
                for item in self.inv:
                    is_equipped = ("Да" if item["is_equipped"] else "Нет") if item["type"] in ("sword", "shield") else None
                    tbl_objects.append([item["name"], f'+{item["pwr"]} {items_ends[item["type"]]}', types_table[item["type"]], is_equipped])

                print(tabulate(tbl_objects, headers=tbl_headers, tablefmt="grid"))
            else:
                print("Твой инвентарь пуст...")
    inventory = Inventory()

    def __init__(self, name, hp=10, lvl=0):
        self.name = name
        self.money = 0

        # Максимально возможное ХП перса
        # ХП перса изначально равно максимальному
        self.hp = hp
        self.maxhp = hp_table[lvl]

        self.lvl = lvl
        self.xp = 0
        self.needXP = xp_table[lvl]

        self.attack = 1
        self.defend = 1

        self.sword = None
        self.shield = None

        self.state = "in city"  # ("in city", "outside", "fight")
        self.is_rested = False
        self.steps = 0

    def fight(self, npc):
        #todo: Rewrite this
        npc_name, npc_lvl, npc_attack, npc_defend, npc_hp = npc.values()
        print(f'Вас атаковал {npc_name}')
        table = [["", "Уровень", "Здоровье", "Атака", "Защита"],
                 [self.name, self.lvl, self.hp, self.attack, self.defend],
                 [npc_name, npc_lvl, npc_hp, npc_attack, npc_defend]]
        print(tabulate(table, headers="firstrow"), "\n")

        inp = input("Провести бой автоматически?\n[Y]es/[N]o: ").lower()
        if inp == "f":
            is_flee_commited = bool(r.randint(0, 1))
            if is_flee_commited:
                print("Тебе удалось избежать боя")
                return True
            else: print("Сбежать не удалось"); input('Enter...')

        auto = True if inp == "y" else False
        while True:
            for item in self.inventory.inv:
                if item["type"] == "hl":
                    heal_index = self.inventory.index(item)
                    heal_in_inventory = True
                    break
            else:
                heal_in_inventory = False

            # Проверяем здоровье. Получаем уровень при победе
            if self.hp <= 0:
                # Юзаем хилку если таковая есть в инвентаре
                if heal_in_inventory:
                    self.use(heal_index)
                else:
                    print(f'{r.choice(ends_fight_lose)}')
                    self.state = "outside"
                    self.get_xp(xp_table[npc_lvl]//2)
                    return False
            elif npc_hp <= 0:
                print(f'{npc_name} {r.choice(ends_fight_win)}')
                self.state = "outside"
                self.get_xp(xp_table[npc_lvl])
                return True
            else:
                # Рандом определяет кто сколько урона получит, учитывая уровень защиты
                pl_dmg = r.randint(0, npc_attack) - r.randint(0, self.defend)
                npc_dmg = r.randint(0, self.attack) - r.randint(0, npc_defend)

                # Учитываем контратаку (отрицательный урон), и обнуляем урон если таковая случилась
                if pl_dmg < 0: npc_dmg -= pl_dmg; pl_dmg = 0
                if npc_dmg < 0: pl_dmg -= npc_dmg; npc_dmg = 0
                # -1 урон это контратака. Соответственно если ты получил -1 урона, твоя защита сыграла на руку и ты дал
                # внеплановых пиздюлей. Или же наоборот, если враг получил -1 урона, то у него свершилось тоже самое и
                # потому лови свою плюху

                # Отнимаем урон от ХП
                self.hp -= pl_dmg
                npc_hp -= npc_dmg

                # В зависимости от полученого урона, выводим соответсвующее сообщение...
                if not auto:
                    clear()
                    if pl_dmg == 0 and npc_dmg == 0:
                        print("Постояли подумали...")
                    elif pl_dmg == 0 and npc_dmg > 0:
                        print(f'Ты нанёс {npc_dmg} урона')
                    elif pl_dmg > 0 and npc_dmg == 0:
                        print(f'Ты получил {pl_dmg} урона')
                    else:
                        print(f'Ты получил {pl_dmg} урона, а нанёс {npc_dmg}\n')
                    print(tabulate([["Имя", "HP"], [self.name, self.hp], [npc_name, npc_hp]], headers="firstrow"))
                    input("Enter...")
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
                # Считаем ХП
            self.maxhp = hp_table[self.lvl]
            self.hp = self.maxhp
            print(f'Ты повысил свой уровень до {self.lvl}, теперь у тебя {self.xp} опыта, и нужно набрать ещё {self.needXP - self.xp}')
        else:
            print(f'Ты получил {xp} XP')
    def get_hp(self, hp):
        if self.hp + hp >= self.maxhp:
            diff = self.maxhp - self.hp
            self.hp = self.maxhp
            print('Здоровье восстановлено до максимального')
            return diff
        else:
            self.hp += hp
            return hp
    # money
    def get_money(self, money):
        self.money += money
        print(f'Ты получил {money} биткоинов')
    def spend_money(self, money):
        self.money -= money
        print(f'Ты потратил {money} биткоинов')

    # items
    def unequip(self, item_type, inv=inventory.inv):
        item_type -= 1
        item = inv[item_type]
        if item['is_equipped']:
            if item['type'] == "sword":
                self.sword = None
                self.attack = 1
            elif item['type'] == "shield":
                self.shield = None
                self.defend = 1
            else: print("У тебя нет экипированного " + ("меча" if item['type'] == "sword" else "щита"))
            inv[item_type]["is_equipped"] = False
            print(f'Ты снял {item["name"]}')
        else:
            print("Нельзя снять ненадетую вещь")
    def use(self, item_index, inv=inventory.inv):
        #todo: Refact this
        item_index -= 1
        item = inv[item_index]
        if item["type"] == "heal":
            old_hp = self.hp
            self.get_hp(item["pwr"])
            inv.remove(item)
            print(f'Ты восстановил {self.hp - old_hp} здоровья, теперь у тебя {self.hp} HP')
        elif item["type"] == "sword":
            if self.sword != None: self.unequip("sword")
            self.sword = item['id']
            self.attack += item["pwr"]
            inv[item_index]['is_equipped'] = True
            print(f'Ты взял в руки {item["name"]}, что увеличело твою атаку до {self.attack}')
        elif item['type'] == "shield":
            if self.shield != None: self.unequip("shield")
            self.shield = item['id']
            self.defend += item["pwr"]
            inv[item_index]['is_equipped'] = True
            print(f'Ты взял в руки {item["name"]}, что увеличело твою защиту до {self.attack}')
        else: print('Ты не можешь использовать эту вещь'); print(item['type'])

    def get_stats(self):
        rows = (
                ['Деньги', self.money],
                ['Опыт', f'{self.xp}/{self.needXP}'],
                ['Уровень', self.lvl],
                ['HP', f'{self.hp}/{self.maxhp}'],
                ['Атака', self.attack],
                ['Защита', self.defend],
                ['____________', '____________'],
        )
        print(tabulate(rows, stralign='left'))