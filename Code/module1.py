# -*- coding: utf-8 -*-

class Plant:

    def check(self): #Revisar si se creo algo
        print("exists")

    #Parametrized constructor
    def __init__(self, n, f,s):
        self.name = n 
        self.frequencyWatering = int(f)
        self.lastWatering = int(s)
        if self.frequencyWatering < self.lastWatering:
            self.needWatering = True
        else:
            self.needWatering = False #Para notificar una única vez
        self.doneWatering = False #Para diferenciar el tiempo de la entrada y la salida de la cola

    def updateLastWatering(self):
        if self.doneWatering == False:
            if self.frequencyWatering <= self.lastWatering: #Entonces sí se necesita agua
                print("         needWatering")
                if self.needWatering == False:
                    #self.notif("Agua")
                    self.needWatering = True
            self.lastWatering += 1
        #Si ya se regó
        else: #doneWaterinf==True
            self.lastWatering = 0
            self.doneWatering = False
            self.needWatering = False

    #Notificaciones, se organizan en colas
    #def notif(str,num):

    # CRUD se implementa por fuera
        