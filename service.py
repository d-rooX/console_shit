import random as r
from clear import clear
from tabulate import tabulate
from tables import *

class NPC:
    def __init__(self, name, hp, attack, defend, lvl):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defend = defend
        self.lvl = lvl


class Player:
    def __init__(self, name, maxhp, lvl, attack, defend):
        self.name = name
        self.money = 0

        # Максимально возможное ХП перса
        # ХП перса изначально равно максимальному
        self.hp = maxhp
        self.maxhp = maxhp

        self.lvl = lvl
        self.xp = 0
        self.needXP = xp_table[lvl]

        self.attack = attack
        self.defend = defend

    class Inventory:
        def __init__(self, size=3):
            self.inv = []
            self.size = size

        def add(self, id):
            if len(self.inv) < self.size:
                item = get_item(id)
                item.update({"id": id})
                self.inv.append(item)
                print(f'Обьект "{item["name"]}" добавлен в инвентарь')
            else:
                print("Инвентарь переполнен")

        def check(self):
            if len(self.inv) > 0:
                tbl_headers = ["Предмет", "Характеристики", "Тип"]
                tbl_objects = []
                for item in self.inv:
                    item_type = item["id"][:2]
                    ends = {"sw":"к максимальному урону", "sh":"к максимальной защите"}
                    tbl_objects.append([item["name"], f'+{item["pwr"]} {ends[item_type]}', types_table[item_type]])
                print(tabulate(tbl_objects, headers=tbl_headers, tablefmt="grid"))
            else:
                print("Твой инвентарь пуст...")

    class Equipment:
        def __init__(self, sword=None, shield=None):
            self.sword = sword
            self.shield = shield

    def fight(self, npc):
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
                print(f'Ты получил {xp_table[npc.lvl]} XP за убийство {npc.name}')
                self.get_xp(npc.lvl)
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

    def get_xp(self, npc_lvl):
        self.xp += xp_table[npc_lvl]
        if self.xp >= self.needXP:
            # тк уровень может повыситься за один раз не только на 1, мы делаем цикл
            while self.xp > self.needXP:
                # Добавляем уровень
                self.lvl += 1
                # Считаем разницу опыта и того который нужен для след. уровня, а потом меняем нужное количество опыта исходя из таблицы
                self.xp -= self.needXP
                self.needXP = xp_table[self.lvl]
            print(
                f'Ты повысил свой уровень до {self.lvl}, теперь у тебя {self.xp} опыта, и нужно набрать ещё {self.needXP - self.xp}')

    def get_money(self, money):
        self.money += money
        print(f'Ты получил {money} биткоинов')

    # todo: def get_status() Которая будет вывдить всю информацию о игроке (деньги, уровень, экипировка, инвентарь)

    inventory = Inventory()
