"""
Plant class and Driver
"""

from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import Hash

hashmap = Hash()
hashmap.Primo_Polynomial()

def agregar_planta():
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant,numParam) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        nameParameter = input("¿Cómo se llama el parámetro " + str(i) + "? ")
        frequencyParameter = int(input("¿Cada cuántas horas se lleva a cabo " + nameParameter + "? "))
        parameter = Parameter(nameParameter, frequencyParameter)
        Plant1.pushBack(parameter)
    hashmap.insert(Plant1)
    #person1.Create(Plant1)

def eliminar_planta(Plant_Name):
    hashmap.Remove(Plant_Name)
    pass
    



agregar_planta()
print(hashmap.Hashtable)
