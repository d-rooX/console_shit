from service import Player, NPC, City
from tables import get_item
from clear import clear
# player = Player(input("Введи имя своего песонажа: ").title(), 10, 0)
# npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 7)
# player.equipment.equip("sw1")
#
# menu = {
#     "inventory":player.inventory.check,
#     "fight":player.fight,
#     # "shop":go_shop
# }
#
# available = ("sw1","sh1","sw2","sh2")
# shop = {
#     "buy":player.inventory.add
# }


city = City()
city.shop.check()
print(city.name)


# while True:
#     clear()
#     print("1) Пойти в магазин")
#     print("2) Пойти на арену")
#     print("3) Посмотреть инвентарь")
#     print("4) Выйти из игры")
#     ch = int(input("Что желаете сделать?\n: "))
#     if ch == 1:
#         while True:
#             clear()
#             print("Выбери предмет: ")
#             print("1) " + get_item("sh1")["name"])
#             print("2) " + get_item("sw4")["name"])
#             print("3) " + get_item("sh3")["name"])
#             print("4) Вернуться")
#             ch1 = int(input(": "))
#             if ch1 in (1, 2, 3):
#                 if ch1 == 1:
#                     player.inventory.add("sh1")
#                 elif ch1 == 2:
#                     player.inventory.add("sw4")
#                 elif ch1 == 3:
#                     player.inventory.add("sh3")
#                 input("Enter...")
#             else:
#                 break
#     elif ch == 2: clear(); player.fight(npc1); input("Enter...")
#     elif ch == 3: clear(); player.inventory.check(); input("Enter...")
#     elif ch == 4: break

