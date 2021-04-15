# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:10:16 2021

@author: mbotello
"""

class plant:
    #Default constructor
    def _init_(self):
        self.frecuencyWatering = 168 #Hours in a week
        self.lastWatering = 24 #a day ago
        if self.frecuencyWatering < self.lastWatering:
            self.needWatering = True
        else: self.needWatering = False
        self.doneWatering=False
        
    #Parametrized constructor
    def _init_(self, f,s,b):
        self.frecuencyWatering = f
        self.lastWatering = s
        if self.frecuencyWatering < self.lastWatering:
            self.needWatering = True
        else: self.needWatering = False
        self.doneWatering = False
        
    #Llamado cada hora o cuando se riega
    def updateLastWatering(self):
        if self.doneWatering == False:
            self.lastWatering += 1
            if self.frequencyWatering < self.lastWatering:
                self.needWatering = True 
                #Preguntar si ya es true sería un paso innecesario
            if self.needWatering:
                self.notif("Agua",)
        #Si se acaba de regar
        else:
            self.lastWatering = 0
         
    #Notificaciones, se organizan en pilas 
    #def notif(str,num):
        
        