import os
from service import Player, NPC
import menu
import time
clear = lambda: os.system('cls')

player = Player("Игнат", 10, 0, 1, 1)
npc1 = NPC("Пидормотский жукотрёп", 7, 1, 1, 0)
