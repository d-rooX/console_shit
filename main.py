from clear import clear
from tables import items_table, get_item
from service import Player, NPC
# import menu
# from story import printStory
# import time

# menu.render()
# printStory("start")

player = Player("Игнат", 10, 0, 1, 1)
npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 0)
print("Выберите: ")
print(get_item("sw1")["name"])
print(get_item("sh2")["name"])
print(get_item("sw3")["name"])
choose = int(input(": "))
if choose == 1:
    player.inventory.add("sw1")

print(player.inventory.inv)

# player.fight(npc1)

