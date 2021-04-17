import time


class Plant:
    def ola(self):
        print("si")
    def __init__(self, f, l):
        self.frecuencyWatering = f
        self.lastWatering = l

    def updateLastWatering(self):
        ver=False
        if self.lastWatering >= self.frecuencyWatering:
            print("Regar Planta Inmediatamente")  #Hay que arreglarlo para que sea .notificacion
            self.lastWatering = 0
            while self.lastWatering < self.frecuencyWatering - 1:
                while self.lastWatering < self.frecuencyWatering - 1:
                    self.lastWatering += 1
                    print(self.lastWatering, 'Días')
                    time.sleep(1)
                print("Regar Planta")
                rep = int(input(("Lo hago despues (0) \n Ya lo hice (1) \n")))
                if rep == 1:
                    self.lastWatering = 0
                else:
                    rep_2 = 0
                    while rep_2 == 0 :
                        time.sleep(1)
                        print ("*Un dia despues*")
                        rep_2 = int(input("Ya? \n 1. Si \n 0. No \n"))
                    if rep_2 == 1:
                        self.lastWatering = 0

        else:
            while self.lastWatering < self.frecuencyWatering:
                while self.lastWatering<self.frecuencyWatering-1:
                    self.lastWatering+=1
                    print(self.lastWatering,'Días')
                    time.sleep(1)
                print("Regar Planta")
                rep = int(input(("Lo hago despues (0) \n Ya lo hice (1) \n")))
                if rep == 1:
                    self.lastWatering=0
                else:
                    rep_2 = 0
                    while rep_2 == 0 :
                        time.sleep(1)
                        print ("*Un dia despues*")
                        rep_2 = int(input("Ya? \n 1. Si \n 0. No \n"))
                    if rep_2 == 1:
                        self.lastWatering = 0


f = int(input('Cada cuantos dias debe ser regada la planta? : '))
l = int(input('Hace cuanto regó la planta? : '))

planta_1 = Plant(f, l)
planta_1.updateLastWatering()
