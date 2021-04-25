# -*- coding: utf-8 -*-

#Clase Persona

class Person:
    
    def check(self):
        print("Exists")
        
    def __init__(self,a):
        self.plantArray = a
    
#----> CRUD

    def Create(self,plant):
        self.plantArray.append(plant)
    
    #Después: CRUD respecto al index
    def Read(self, string):
        a = self.plantArray[self.Search(string)]
        print("La planta con nombre" , a.name, "y parámetros", a.param)
    
    def Update(self, string):#Esto queda bien? Podríamos editar un parámetro en específico o algo así
        self.Delete(string)
        self.Create()
    
    def Delete(self, string):
        self.plantArray.pop(self.Search(string))
    
    def Search(self, string):#Tal vez podríamos organizar en orden alfabético
        ran = len(self.plantArray)
        for i in range(ran):
            if (string == self.plantArray[i].name):
                return i
        