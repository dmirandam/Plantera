# -*- coding: utf-8 -*-
"""
Plant class and Driver
"""
from linkedlist import LinkedList
from Heap import MinHeap
from HashMap import HashTable

class Plant(LinkedList): #define la clase planta con sus distintos parámetros 
    def __init__(self, n, np):
        super().__init__()
        self.Name = n  
        self.NumberParam = np
        #self.pushBack(p)  #parametros
        #falta cola
        
class Parameter():
    def __init__(self, name, frequency):
        self.Name = name 
        self.Frequency = frequency 
        self.Next = self.Frequency

#--------->

def Create():
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant,numParam) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        nameParameter = input("¿Cómo se llama el parámetro " + str(i) + "? ")
        frequencyParameter = int(input("¿Cada cuántas horas se lleva a cabo " + nameParameter + "? "))
        parameter = Parameter(nameParameter, frequencyParameter)
        Plant1.pushBack(parameter)
        tasks.Insert(parameter)
    #person1.Create(Plant1)
    
#-----------> Driver

tasks = MinHeap()
Create()


        
        