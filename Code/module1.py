# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:10:16 2021

@author: mbotello
"""

class Plant:

    def check(self):
        print("exists")
    #Esto es para ofrecer un demo
    def __init__(self):
        self.name = "Rose"
        self.frecuencyWatering = 168 #Hours in a week
        self.lastWatering = 24 #a day ago
        if self.frecuencyWatering < self.lastWatering:
            self.needWatering = True
        else: self.needWatering = False
        self.doneWatering = False

    #Parametrized constructor
    def __init__(self, n, f,s):
        self.name = n
        self.frequencyWatering = int(f)
        self.lastWatering = int(s)
        if self.frequencyWatering < self.lastWatering:
            self.needWatering = True
        else:
            self.needWatering = False #Para notificar una única vez
            self.doneWatering = False #Para diferenciar el tiempo de la notificación al de la regada

    #Llamado cada hora o cuando se riega

    def updateLastWatering(self):
        if self.doneWatering == False:
            if self.frequencyWatering < self.lastWatering:
                print("         needWatering")
                if self.needWatering == False:
                    #self.notif("Agua")
                    self.needWatering = True
            self.lastWatering += 1
        #Si ya se regó
        else:
            self.lastWatering = 0
            self.doneWatering = False
            self.needWatering = False

    #Notificaciones, se organizan en pilas
    #def notif(str,num):

        