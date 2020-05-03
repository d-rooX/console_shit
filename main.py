from service import Player, NPC, City
from clear import clear

player = Player("Игнат")
npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 7)
city = City()

commands = {
    "inventory_check": player.inventory.check,  # empty
    "clear": clear,                             # empty
    "get_stats": player.get_stats,              # empty
    "shop": city.shop.check,                    # empty

    "get_money": player.get_money,              # money
    "take_money": player.spend_money,           # money

    "get_xp": player.get_xp,                    # xp

    "equip": player.equip,                      # item_index

    "buy": player.buy,                          # !shop, item_index
    "fight": player.fight,                      # !NPC
    "inventory_add": player.inventory.add,      # !item
}

#todo: def do_commands()

