from service import Player, City
from clear import clear
from tables import get_item, npc_table, hp_table
import random as r

player = Player("DAne4ka")
city = City()

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
        player.state = "outside"
        clear()
        print(f'Ты покинул {city.name}')
    else:
        situation = r.choice(("pass", "pass", "pass", "pass", "attack", "attack", "attack", "trap", "trap", "city", "city", "chest"))
        if situation == "attack":
            npc = npc_table[r.randint(0, player.lvl + 1)]  # Ловим уровень НПС
            hp_range = (hp_table[npc["lvl"]] // 2, hp_table[npc["lvl"]])  # Ловим хп НПС
            npc.update({"hp": r.randint(*hp_range)})  # Добавляем ХП в обьект НПС, так как изначально его там нет
            player.fight(npc)  # воюем
        elif situation == "trap":
            print("trap")
        elif situation == "city":
            city.generate()
            if input(f'Ты прибыл в город {city.name}, остановиться?\n[Y]es/[N]o: ') in ("Y", "y"):
                player.state = "in city"
                print(f'Ты в городе {city.name}. Уровень его экономики - {city.economics}')
        elif situation == "chest":
            coins = r.randint(5,100)
            print(f"Ты нашёл {coins} биткоинов.")
            player.money += coins
        else:
            print("Ты спокойно погулял по полям")

commands = {
        "inventory_check": player.inventory.check,  # empty
        "clear":           clear,  # empty
        "get_stats":       player.get_stats,  # empty
        "shop":            city.check,  # empty
        "walk":            walk,  # empty

        "get_money":       player.get_money,  # money!
        "spend_money":     player.spend_money,  # money!
        "get_xp":          player.get_xp,  # xp!
        "inventory_add":   player.inventory.add,  # item!

        "unequip":         player.unequip,  # item_index
        "equip":           player.equip,  # item_index
        "use":             player.use,  # item_index
        "buy":             buy,  # item_index

        "fight":           player.fight,  # !NPC
}

while True:
    try:
        com = input(': ').split()
        command = com[0]
        argument = (int(com[1]) if com[1].isnumeric() else com[1]) if len(com) > 1 else False
        commands[command](argument) if argument else commands[command]()
    except Exception as e:
        raise e
