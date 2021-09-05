# -*- coding: utf-8 -*-
"""
Plant and Parameter
"""
from linkedlist import LinkedList

class Plant(LinkedList): #define la clase planta con sus distintos parámetros 
    def __init__(self, n):
        super().__init__()
        self.Name = n
        #self.pushBack(p)  #parametros
        #falta cola
        
class Parameter():
    def __init__(self, name, frequency, plant):
        self.Name = name 
        self.Frequency = frequency 
        self.Next = self.Frequency
        self.Plant = plant