from service import Player, City
from clear import clear
from tables import get_item, npc_table, hp_table
import random as r

player = Player("11", 5)
city = City()
player.inventory.add(get_item("hl1"))

def go_out():
    if player.state not in ("outside"):
        player.state = "outside"
        print(f"Ты покинул {city.name}, и отправился в путешествие")
        while player.state == "outside":

            # 5 пропуск 3 нападение 2 ловушка 1 город
            situation = r.choice(("pass", "pass", "pass", "pass", "pass",
                                  "attack", "attack", "attack",
                                  "trap", "trap",
                                  "city"))
            if situation == "attack":
                player.state = "fight"
                npc = npc_table[r.randint(0, player.lvl+1)]
                hp_range = (hp_table[npc["lvl"]]//2, hp_table[npc["lvl"]])
                npc.update({"hp":r.randint(*hp_range)})
                player.fight(npc)
            elif situation == "trap":
                print("trap")
            elif situation == "city":
                city.generate()
                if input(f'Ты прибыл в город {city.name}, остановиться?\n[Д]а, [Н]ет: ') in ("Д", "д"):
                    player.state = "in city"
                    break
            else:
                print("Ты спокойно погулял по полям")
                # todo:random
    else:
        print("Куда ещё дальше то?") if player.state == "outside" else print("Ты сейчас в драке, свалить не получиться")

commands = {
        "inventory_check": player.inventory.check,  # empty
        "clear":           clear,  # empty
        "get_stats":       player.get_stats,  # empty
        "shop":            city.check,  # empty

        "get_money":       player.get_money,  # money!
        "spend_money":     player.spend_money,  # money!
        "get_xp":          player.get_xp,  # xp!
        "inventory_add":   player.inventory.add,  # item!

        "unequip":         player.unequip,  # item_index
        "equip":           player.equip,  # item_index
        "use":             player.use,  # item_index

        "buy":             player.buy,  # !shop, item_index
        "fight":           player.fight,  # !NPC
        "go_out":          go_out
}

def do_commands(com: str):
    com = com.split()
    command = com[0]
    argument = (int(com[1]) if com[1].isnumeric() else com[1]) if len(com) > 1 else False
    commands[command](argument) if argument else commands[command]()

while True:
    do_commands(input(': '))