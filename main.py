from service import Player, City
from clear import clear
from tables import get_item, npc_table, hp_table
import random as r
from colors import print_color

player = Player("DAne4ka")
city = City()
player.inventory.add(get_item("hl2"))
player.inventory.add(get_item("sw4"))
city.check_city()

def is_agree():
    return True if input('[Y]es/[N]o: ').replace(' ', '').lower() == 'y' else False

def work():
    if city.is_job and not city.is_job_completed:
        print('Ты нашёл кого то, кому требуется помощь, и выполнил это непростое поручение')
        print(f'В награду ты получил {city.payment} биткоинов')
        player.money += city.payment
        city.is_job_completed = True
    else: print('В городе нет подработки')

def buy(item_index):
    item_index -= 1
    if player.state == "in city":
        assortment = city.assortment
        if city.amount > 0 and assortment[item_index]["price"] <= player.money:
            player.inventory.add(assortment[item_index])
            player.spend_money(assortment[item_index]["price"])
        else:
            print("Ты не можешь купить эту вещь")
    else:
        print("Ты не в городе")

def walk():
    if player.state != "outside":
        if player.hp > 0:
            player.state = "outside"
            clear()
            print(f'Ты покинул {city.name}')
        else: print('У тебя совсем нет HP, полечись немного')
    else:
        player.steps += 1 #todo: Нахера я это применял?
        situation = r.choice(("pass", "pass", "pass", "pass", "attack", "attack", "attack", "trap", "trap", "city", "city", "chest"))
        if situation == "attack":
            npc = npc_table[r.randint(0, player.lvl + 1)]  # Ловим уровень НПС
            npc['hp'] = r.randint(hp_table[npc["lvl"]] // 2, hp_table[npc["lvl"]])  # Добавляем ХП в обьект НПС, так как изначально его там нет
            if not player.fight(npc): # воюем
                print('Тебя обессиленного дотащили в ближайший город')
                input("Enter...")
                clear()
                city.generate()
                city.check_city()
                player.state = "in city"
        elif situation == "trap":
            dmg = r.randint(1, player.hp//3)
            player.hp -= dmg
            print(f'Тебя укусила змея! Не очень приятно, ибо ты потерял {dmg} HP.')
        elif situation == "city":
            city.generate()
            print(f'Ты прибыл в город {city.name}, остановиться?')
            if is_agree():
                player.state = "in city"
                player.steps = 0
                clear()
                city.check_city()
        elif situation == "chest":
            coins = r.randint(1, 100)
            print('Гуляя по очередному полю, ты нашёл странный сундук. Хотя не такой уж он и странный, если учесть что там были деньги...')
            print(f'Найдено {coins} биткоинов')
            player.money += coins
        else:
            print("Ты спокойно погулял по полям")

def rest():
    if city.hotel:
        print('Ты хочешь отдохнуть в отеле?')
        if is_agree():
            print(f'Стоимость ночи в отеле этого города {city.hotel_cost} биткоинов. Согласится?')
            if is_agree():
                if player.money >= city.hotel_cost:
                    player.is_rested = True
                    rested = r.randint(player.maxhp // 2, int(player.maxhp // 1.5)) if city.economics == 'medium'\
                        else r.randint(int(player.maxhp // 1.1), player.maxhp)
                    rested = player.get_hp(rested)
                    print(f'Ты отдохнул в отеле и восстановил {rested} HP')
                else: print('У тебя не хватает биткоинов')
    else:
        if not player.is_rested:
            print('Отдохнуть под открытым небом?')
            if is_agree():
                player.is_rested = True
                rested = r.randint(2, int(player.maxhp // 2.5))
                rested = player.get_hp(rested)
                print(f'Ты разбил палатку и немного отдохнул. Восстановлено {rested} HP')
        else: print("Ты уже отдыхал. Пройдись хоть немного!")

def help_commands():
    coms = {'inventory':'Показать инвентарь',
            'clear':'Очистить дисплей',
            'stats':'Вывести информацию о персонаже',
            'shop':'Показать ассортимент магазина в городе',
            'walk':'Выйти на улицу\Пойти дальше',
            'rest':'Отдохнуть',
            'city':'Вывести информацию о городе',
            'unequip':'Снять вещь',
            'use':'Надеть\Использовать вещь',
            'buy':'Купить вещь в магазине',
            'get_money':'',
            'spend_money':'',
            'get_xp':'',
            'inventory_add':'',
            'help':'Вывести это окно'}
    for key in coms:
        print(f'{key} - {coms[key]}')

commands = {
        "inventory":       player.inventory.check,  # empty
        "clear":           clear,  # empty
        "stats":           player.get_stats,  # empty
        "shop":            city.check_shop,  # empty
        "walk":            walk,  # empty
        "work":            work, # empty
        "rest":            rest, # empty
        "city":            city.check_city, # empty

        "unequip":         player.unequip,  # item_index
        "use":             player.use,  # item_index
        "buy":             buy,  # item_index

        "get_money":       player.get_money,  # money!
        "spend_money":     player.spend_money,  # money!
        "get_xp":          player.get_xp,  # xp!
        "inventory_add":   player.inventory.add,  # item!

        "help":            help_commands
}

while True:
    try:
        com = input(': ').lower().split()
        if len(com) > 0:
            command = com[0]
            argument = (int(com[1]) if com[1].isnumeric() else com[1]) if len(com) > 1 else False
            commands[command](argument) if argument else commands[command]()
        else:
            continue
    except IndexError:
        print('Введён неверный порядковый номер предмета')
    except KeyError:
        print('Нет такой команды')
    except: print('Ошибка. Возможно перед командой ты поставил пробел')

