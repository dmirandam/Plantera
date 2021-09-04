"""
Plant class and Driver
"""

from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import Hash

hashmap = Hash()
hashmap.Primo_Polynomial()

def Plant_Create():
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant,numParam) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        nameParameter = input("¿Cómo se llama el parámetro " + str(i) + "? ")
        frequencyParameter = int(input("¿Cada cuántas horas se lleva a cabo " + nameParameter + "? "))
        parameter = Parameter(nameParameter, frequencyParameter)
        Plant1.pushBack(parameter)
    hashmap.Insert(Plant1.Name)
    return Plant1

def Plant_Read(Plant):
    print(Plant.Name, "tiene", Plant.length, "parámetros:")
    print("Nombre   Frecuencia   Próxima acción")
    var = Plant.head
    while var != None:
        x = var.key #Parámetro
        print(x.Name, "  ", x.Frequency, "  ", x.Next)
        var = var.next
    print(" ")

def Plant_Update(Plant):
    
    pass

def Plant_Delete(Plant):
    hashmap.Remove(Plant.Name)
  
#------>

Plant = Plant_Create()
print(hashmap.Hashtable)
Plant_Read(Plant)
Plant_Delete(Plant)
print(hashmap.Hashtable)

