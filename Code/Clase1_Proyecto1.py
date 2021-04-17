import time


class Plant:

    def __init__(self, f, l):
        self.frecuencyWatering = f
        self.lastWatering = l

    def updateLastWatering(self):
        ver=False
        if self.lastWatering >= self.frecuencyWatering:
            print("Regar Planta")  #Hay que arreglarlo para que sea .notificacion
            ver = True
        else:
            while self.lastWatering<self.frecuencyWatering-1:
                self.lastWatering+=1
                print(self.lastWatering,'Días')
                time.sleep(1)
            if not ver:
                print("Regar Planta")


f = int(input('Cada cuantos dias debe ser regada la planta? : '))
l = int(input('Hace cuanto regó la planta? : '))

planta_1 = Plant(f, l)
planta_1.updateLastWatering()
