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
        import pygame
        Window = pygame.display.set_mode(Display)

        Radiuse = 150 #Ширина, высота графика
        Distance = Radiuse // (600 / 4) #6
        Centre = [Display[0]//2, Display[1]//2-40] #300x, 200y  #Центр графика-квадрата
        UpLeft = [Centre[0]-Radiuse//2, Centre[1]-Radiuse//2] #225x, 125y  #Верхний левый угол графика-квадрата

        #Данные точек на гранях квадрата
        Limite = []
        for i in range(150): #Up
            Limite.append([UpLeft[0] + Distance*i, UpLeft[1]])
        for i in range(150): #Right
            Limite.append([UpLeft[0]+Radiuse, UpLeft[1] + Distance*i])
        for i in range(150): #Down
            Limite.append([UpLeft[0]+Radiuse - Distance*i, UpLeft[1]+Radiuse])
        for i in range(150): #Left
            Limite.append([UpLeft[0], UpLeft[1]+Radiuse - Distance*i])

        #Проценты
        Procent = []
        for i in range(len(Info)):
            Procent.append(int(Info[i] / sum(Info) * 100) / 100)
        if sum(Procent) == 0.99: #Округление
             Cash = max(Procent)
             Procent.remove(Cash)
             Cash += 0.01
             Procent.append(Cash)
        #Пеетосовка
        for i in range(len(Procent)): #Прпоценты
            if i == 0:
                Cash2 = Procent
                Cash = []
            Cash.append(max(Cash2))
            Cash2.remove(min(Cash))
            if i == len(Procent):
                Procent = Cash
        for i in range(len(Info)): #Данные
            if i == 0:
                Cash2 = Info
                Cash = []
            Cash.append(max(Cash2))
            Cash2.remove(min(Cash))
            if i == len(Info):
                Info = Cash

        Cash = Limite

        EndPoint = []
        for i in range(len(Procent)):
            EndPoint.append(int(600 * Procent[i]))

        Reincarnation = False

        while not end:
            Limite = Cash
            Window.fill(Color["Fone"])
            pygame.draw.rect(Window, Color["Grid"], (UpLeft[0], UpLeft[1], Radiuse, Radiuse))
            for i in range(len(Procent)):
                for q in range(int(Procent[i]*600)):
                    if Reincarnation:
                        print("Start")
                        q = EndPoint[i]-1
                    #pygame.draw.line(Window, RandColor[i], (Centre[0], Centre[1]), (Limite[q][0], Limite[q][1]))
                    if q == EndPoint[i]-1:
                        print("New")
                        Reincarnation = True

            pygame.draw.line(Window, RandColor[0], (Centre[0], Centre[1]), (Limite[EndPoint[0]][0], Limite[EndPoint[0]][1]))
            pygame.draw.line(Window, RandColor[1], (Centre[0], Centre[1]), (Limite[EndPoint[1]][0], Limite[EndPoint[1]][1]))
            pygame.draw.line(Window, RandColor[2], (Centre[0], Centre[1]), (Limite[EndPoint[2]][0], Limite[EndPoint[2]][1]))

            #for i in range(len(Limite)):
            #    pygame.draw.line(Window, LowColor["Blue"], (Centre[0], Centre[1]), (Limite[i][0], Limite[i][1]))

            pygame.display.update()

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    end = True
                    pygame.display.quit()
                    pygame.quit()

    elif com == "5" and len(Info) == 0:
        print("\n Для построения графика нужны данные")

    #Настройки
    while com == "6":
        if OneReturn:
            print("|\n|Введите \"end\" для выхода из настроек")
            OneReturn = False

        com = input("|\n| 1. Фон - " + str(Settings[5]) + "\n| comand >")
        if com == "end":
            break

        #Фон
        elif com == "1":
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
