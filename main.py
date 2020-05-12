from service import Player, City
from clear import clear
from tables import get_item, npc_table, hp_table
import random as r

player = Player("DAne4ka")
city = City()
player.inventory.add(get_item("hl2"))
player.inventory.add(get_item("sw4"))
city.check_city()

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
        situation = r.choice(("pass", "pass", "pass", "pass", "attack", "attack", "attack", "trap", "trap", "city", "city", "chest"))
        if situation == "attack":
            npc = npc_table[r.randint(0, player.lvl + 1)]  # Ловим уровень НПС
            npc['hp'] = r.randint(hp_table[npc["lvl"]] // 2, hp_table[npc["lvl"]])  # Добавляем ХП в обьект НПС, так как изначально его там нет
            if not player.fight(npc): # воюем
                print('Тебя обессиленного дотащили в ближайший город')
                input("Enter...")
                player.state = "in city"
                clear()
        elif situation == "trap":
            dmg = r.randint(1, player.hp//3)
            player.hp -= dmg
            print(f'Тебя укусила змея! Не очень приятно, ибо ты потерял {dmg} HP.')
        elif situation == "city":
            city.generate()
            if input(f'Ты прибыл в город {city.name}, остановиться?\n[Y]es/[N]o: ').replace(' ', '') in ("Y", "y"):
                player.state = "in city"
                clear()
                city.check_city()
        elif situation == "chest":
            coins = r.randint(1,50)
            print('Гуляя по очередному полю, ты нашёл странный сундук. Хотя не такой уж он и странный, если учесть что там были деньги...')
            player.money += coins
        else:
            print("Ты спокойно погулял по полям")
def rest():
    if input('Ты хочешь отдохнуть в отеле?\n[Y]es/[N]o:'):
        if city.hotel and city.hotel_cost <= player.money:
            if input(f'Стоимость ночи в отеле этого города {city.hotel_cost} биткоинов. Согласится?\n[Y]es/[N]o: ').lower() == 'y':
                rested = r.randint(player.maxhp // 2, player.maxhp // 1.5) if city.hotel == 'motel' else r.randint(player.maxhp // 1.5, player.maxhp)
                res = player.hp + rested
                player.hp = res if res <= player.maxhp else player.maxhp
                print(f'Ты отдохнул в отеле и восстановил {res} HP')
        else: print('У тебя не хватает биткоинов или в городе нет отеля.')
    else:
        if input('Отдохнуть под открытым небом?\n[Y]es/[N]o: ').lower() == 'y':
            player.state = "resting"
            rested = r.randint(2, player.maxhp // 2)
            player.get_hp(rested)
            print(f'Ты разбил палатку и немного отдохнул. Восстановлено {rested} HP')
def help_commands():
    coms = ''
    for key in commands.keys():
        coms += f"'{key}', "
    print(coms)

commands = {
        "inventory":       player.inventory.check,  # empty
        "clear":           clear,  # empty
        "stats":           player.get_stats,  # empty
        "shop":            city.check_shop,  # empty
        "walk":            walk,  # empty
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
        com = input(': ').split()
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
