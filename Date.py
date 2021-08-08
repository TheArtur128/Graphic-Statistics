from random import randint as rand
from Setting import *

Info = [] #Данные для графика

end = False
OneReturn = True

Display = [600, 400]

def New(Com):
    if Com == "Color":
        return (rand(0, 255), rand(0, 255), rand(0, 255))

RandColor = []
for i in range(600):
    RandColor.append(New("Color"))

if Settings[5]: #White fone
    Color = {
    "Fone": (255, 255, 255),
    "Grid": (235, 235, 235)
    }

elif not Settings[5]: #Black fone
    Color = {
    "Fone": (30, 30, 30),
    "Grid": (20, 20, 20)
    }

LowColor = {
    "Red": (225, 23, 92),
    "Blue": (0, 128, 255),
    "Green": (0, 244, 129),
    "Purpure": (204, 0, 255),
    "Viiolet": (128, 0, 255)
    }

RandColor = [(225, 23, 92), (0, 128, 255), (0, 244, 129), (204, 0, 255), (128, 0, 255)]

Welcome = ("\n1. - Ввести данные вручную через консоль\n2. - Взять данные из Setting.py\n3. - Очистить данные\n4. - Показать данные для графика\n5. - Начать построение графика\n6. - Настройки\n7. - Выход\ncomand >")
