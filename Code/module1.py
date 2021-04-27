# -*- coding: utf-8 -*-


#Exactamente igual, solo se cambiaron los nombres
#    param[i] es el parámetro i
#    param[i][0] <- nombre del parámetro, nueva variable
#    param[i][1] <- frequencyWatering
#    param[i][2] <- lastWatering
#    param[i][3] <- needWatering
#    param[i][4] <- doneWatering

class Plant:

    def check(self): #Revisar si se creo algo
        print("exists")
    
    #Parametrized constructor
    def __init__(self, n, np, p):
        self.name = n
        self.numberParam = np
        #param es una lista que contiene a cada parámetro
        #Cada parámetro es una lista que contiene la info Name, frequency, last, need, done
        #Lo que antes era FrequencyWatering, lastWatering, needWatering, doneWatering
        self.param = p
        self.cola = {}


    def updateParameteri(self,i):
        #Exactamente igual a updateWatering, solo se cambiaron los nombres correspondientes
        if self.param[i][4] == False:
            if self.param[i][1]-3 < self.param[i][2]: #Entonces sí se necesita agua
                if self.param[i][3] == False:
                    self.cola[self.param[i][0]] = 0
                    self.param[i][3] = True
            self.param[i][2] += 1
        
        #Si se acaba de regar
        else: 
            self.param[i][2] = 0
            self.param[i][4] = False
            self.param[i][3] = False

    #Notificaciones, se organizan en colas
    
    def notif(self):
      print ("              ***NOTIFICACIONES***")
      for i in self.cola:
        if self.cola[i] == 0:
          print("debes", i, "a", self.name)
        else:
          print("debes",i, "a", self.name, "tuviste que hacerlo hace:", self.cola[i], "horas")
        self.cola[i] += 1
    
    def Desnotif(self,a):
      for i in self.cola:
        if a == i:
          del self.cola[i]
          print("           Has hecho",a," a",self.name)
          break


        
        #Si se acaba de regar
        else: 
            self.param[i][2] = 0
            self.param[i][4] = False
            self.param[i][3] = False

    #Notificaciones, se organizan en colas
    #def notif(str,num):

    # CRUD 
