story = {
    "start": "Привет. \\ Я не знаю зачем ты в это вообще играешь. \\ Я не знаю откуда у тебя эта залупа на ПК... \\"
}


def printStory(key):
    for part in story[key].split("\\"):
        print(part)
        input()
