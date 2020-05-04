from service import Player, NPC, City
from clear import clear
from tables import get_item

player = Player("Игнат")
npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 7)
city = City()

commands = {
        "inventory_check": player.inventory.check,  # empty
        "clear":           clear,  # empty
        "get_stats":       player.get_stats,  # empty
        "shop":            city.shop.check,  # empty

        "get_money":       player.get_money,  # money!
        "spend_money":     player.spend_money,  # money!

        "get_xp":          player.get_xp,  # xp!

        "unequip":         player.unequip,
        "equip":           player.equip,  # item_index
        "use":             player.use,  # item_index

        "buy":             player.buy,  # !shop, item_index
        "fight":           player.fight,  # !NPC
        "inventory_add":   player.inventory.add,  # item!
}

# todo: def do_commands()

player.inventory.add(get_item("sw1"))
player.inventory.add(get_item("sw2"))
player.inventory.check()
player.equip(0)
player.inventory.check()
player.equip(1)
player.inventory.check()