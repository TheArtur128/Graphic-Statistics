from Date import *

print("Можете построить график из данных в Setting.py, только введите туда данные в квадратные скобки через запятую.\n\nВведите команду")
while True:
    com = input(Welcome)

    #Ручной ввод
    while com == "1":
        if OneReturn:
            print("|\n|Введите \"end\" для завершения ввода данных")
            OneReturn = False
        cash = input("|\n| Info >")
        #Заканчиваем ввод
        if cash == "end":
            break

        #Проверка ввели ли число
        try:
            Info.append(float(cash))
        except:
            print("| Eror, введите число")

    #Вводим данные из List
    if com == "2":
        Info = List

    #Очищаем данные
    if com == "3":
        Info = []

    #Просмотр данных
    if com == "4":
        print("\n" + str(Info))

    #Построение графика
    if com == "5" and len(Info) != 0:
        print("\nOne seconds...\n")
        import pygame
        OldPoint = [0, Display[1]]
        Coficent = Display[1] // max(Info) #Средняя высота точки\клетки
        Distance = Display[0] // len(Info) #Среднее растояние точки\клетки

        Window = pygame.display.set_mode(Display)
        pygame.display.set_caption("Graphix")
        clock = pygame.time.Clock()

        while not end:
            clock.tick(30)

            Window.fill(Color["Fone"])

            #Прорисовка
            for i in range(1, len(Info) + 1):
                #Сетка горизонтальная
                if Settings[2]:
                    for q in range(int(max(Info))):
                        pygame.draw.line(Window, (Color["Grid"]), (0, Display[1]/max(Info) * q), (Display[0], Display[1]/max(Info) * q), 2)
                #Сетка вертикальная
                if Settings[3]:
                    for q in range(len(Info)):
                        pygame.draw.line(Window, (Color["Grid"]), (Distance * i, 0), (Distance * i, Display[1]), 2)

                #Line
                if i == 1 and Settings[4]: #Фиксируем начало
                    OldPoint = [0, Display[1] - Coficent * Info[i-1]]
                pygame.draw.line(Window, (15, 141, 255), (OldPoint), (Distance * i, Display[1] - Coficent * Info[i-1]), 5)

                #Точки
                if Settings[0]:
                    pygame.draw.rect(Window, (0, 112, 213), (Distance * i - 3, Display[1] - Coficent * Info[i-1] - 1, 5, 10))

                #Ставим первую точку отрезка на начальное место
                if i == len(Info):
                    OldPoint = [0, Display[1]]
                else:
                    OldPoint = [Distance * i, Display[1] - Coficent * Info[i-1]]

            pygame.display.update()

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    end = True
                    pygame.display.quit()
                    pygame.quit()

        end = False

    elif com == "5" and len(Info) == 0:
        print("\n Для построения графика нужны данные")

    #Настройки
    while com == "6":
        if OneReturn:
            print("|\n|Введите \"end\" для выхода из настроек")
            OneReturn = False

        com = input("|\n| 1. Точки на графике - " + str(Settings[0]) + "\n| 2. Горизонтальная сетка - " + str(Settings[2]) + "\n| 3. Вертикальная сетка - " + str(Settings[3]) + "\n| 4. Запоздание начало графика - " + str(Settings[4]) + "\n| 5. Фон - " + str(Settings[5]) + "\n| comand >")
        if com == "end":
            break

        #Точки
        elif com == "1":
            if Settings[0]:
                Settings[0] = False
            else:
                Settings[0] = True

        #Сетка горизонтальная
        elif com == "2":
            if Settings[2]:
                Settings[2] = False
            else:
                Settings[2] = True

        #Сетка вертикальная
        elif com == "3":
            if Settings[3]:
                Settings[3] = False
            else:
                Settings[3] = True

        #Запоздание
        elif com == "4":
            if Settings[4]:
                Settings[4] = False
            else:
                Settings[4] = True

        #Фон
        elif com == "5":
            if Settings[5]: #Тёмный
                Settings[5] = False #Запоминаем тему фона на след. запуск

                Color = {
                "Fone": (30, 30, 30),
                "Grid": (20, 20, 20)
                }
            else: #Светлый
                Settings[5] = True

                Color = {
                "Fone": (255, 255, 255),
                "Grid": (235, 235, 235)
                }


        com = "6"

    #Выход
    if com == "7":
        open("Setting.py", "w").write("List = " + str(List) + "\nSettings = " + str(Settings))
        open("Setting.py").close
        break
