import os
from service import Player, NPC
import menu
from story import printStory
import time
clear = lambda: os.system('cls')

# menu.render()
# printStory("start")

player = Player("Игнат", 10, 0, 1, 1)
npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 0)

input(" ")
# player.fight(npc1)

