import random as r
import os
from prettytable import PrettyTable

clear = lambda: os.system('cls')
xp_table = {0: 10, 1: 20, 2: 30, 3: 50, 4: 100, 5: 200, 6: 350, 7: 500}
tbl = PrettyTable()

class NPC:
    def __init__(self, name, hp, lvl, attack, defend):
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
        self.maxhp = maxhp
        self.hp = maxhp

        self.lvl = lvl
        self.xp = 0
        self.needXP = xp_table[lvl]

        self.attack = attack
        self.defend = defend

    def fight(self, NPC):
        # Описываем все нужные значения
        npc_hp = NPC.hp
        npc_attack = NPC.attack
        npc_defend = NPC.defend
        npc_lvl = NPC.lvl
        npc_name = NPC.name

        print(f'Вы атаковали {npc_name}')
        tbl.field_names = ["", "Уровень", "Здоровье", "Атака", "Защита"]
        tbl.add_row([self.name, self.lvl, self.hp, self.attack, self.defend])
        tbl.add_row([npc_name, npc_lvl, npc_hp, npc_attack, npc_defend])
        print(tbl)
        input()
        while True:
            # чистим консоль
            clear()

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
            if pl_dmg == 0 and npc_dmg == 0:
                print("Постояли подумали...")
            elif pl_dmg == 0 and npc_dmg > 0:
                print(f'Ты нанёс {npc_dmg} урона')
            elif pl_dmg > 0 and npc_dmg == 0:
                print(f'Ты получил {pl_dmg} урона')
            else:
                print(f'Ты получил {pl_dmg} урона, а нанёс {npc_dmg}')
            input(f'У тебя {self.hp} HP, у противника {npc_hp}\n')

            # Проверяем здоровье. Получаем уровень при победе
            if self.hp <= 0:
                print(f'Ты проиграл этот бой')
                break
            if npc_hp <= 0:
                print(f'Ты победил. У тебя {self.hp} HP')
                print(f'Ты получил {xp_table[npc_lvl]} XP за убийство {npc_name}')
                self.getxp(npc_lvl)
                break

    def getxp(self, npc_lvl):
        self.xp += xp_table[npc_lvl]
        if self.xp >= self.needXP:
            # Добавляем уровень
            self.lvl += 1
            # Считаем разницу опыта и того который нужен для след. уровня, а потом меняем нужное количество опыта исходя из таблицы
            self.xp -= self.needXP
            self.needXP = xp_table[self.lvl]
            print(f'Ты повысил свой уровень до {self.lvl}, теперь у тебя {self.xp} опыта, и нужно набрать ещё {self.needXP-self.xp}')

    def getmoney(self, money):
        self.money += money
        print(f'Ты получил {money} биткоинов')
