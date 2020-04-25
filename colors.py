from ctypes import *


def color(text, color):
    windll.Kernel32.GetStdHandle.restype = c_ulong
    h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
    colors = {
        "blue": 1,
        "green": 2,
        "cyan": 3,
        "red": 4,
        "pink": 13,
        "yellow": 6,
        "dark": 8,
        "light": 14,
    }
    windll.Kernel32.SetConsoleTextAttribute(h, colors[color])
    print(text)
    windll.Kernel32.SetConsoleTextAttribute(h, 0)


color("hello", "red")
color("whats up?", "light")
