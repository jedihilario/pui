import os
from readchar import readkey, key

colors = {
    'black' : '\33[30m',
    'red' : '\33[31m',
    'green' : '\33[32m',
    'yellow' : '\33[32m',
    'blue' : '\33[34m',
    'white' : '\33[37m'
}

class Title:
    def __init__(self, content, color = 'white', paddingX = 0, paddingY = 0, paddingFill = ' ') -> None:
        self.content = content
        self.color = colors[color]
        self.paddingX = paddingX
        self.paddingY = paddingY
        self.paddingFill = paddingFill

    def render(self) -> None:
        for i in range(self.paddingY + 1):
            for j in range(self.paddingX + len(self.content)):
                if(i == self.paddingY // 2 and j == self.paddingX // 2):
                    print(f'{self.color}{self.content}{colors["white"]}', end='')
                    print(self.paddingFill * (self.paddingX // 2), end='')
                    break
                print(self.paddingFill, end='')
            print()

class optionsMenu:
    def __init__(self, options, optionsCallbacks, cursorChar = '<', cursorColor = 'blue') -> None:
        self.options = options.copy()
        self.optionsCallbacks = optionsCallbacks.copy()
        self.cursorChar = cursorChar
        self.cursorColor = cursorColor
        self.cursorPosition = 0

    def draw(self) -> None:
        for i in range(len(self.options)):
            print(self.options[i], end='')
            if(i == self.cursorPosition):
                print(f'{colors[self.cursorColor]}{self.cursorChar}{colors["white"]}', end='')
            print()

    def render(self, components) -> None:
        wait = True
        self.draw()
        while(wait):
            k = readkey()
            if(k == key.UP):
                if(self.cursorPosition > 0):
                    self.cursorPosition -= 1
                    os.system('cls')
                    for i in components: i.render()
                    self.draw()
            elif(k == key.DOWN):
                if(self.cursorPosition < len(self.options) - 1):
                    self.cursorPosition += 1
                    os.system('cls')
                    for i in components: i.render()
                    self.draw()
            elif(k == key.ENTER):
                os.system('cls')
                self.optionsCallbacks[self.cursorPosition]()
                wait = False