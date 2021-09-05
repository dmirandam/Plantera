"""
Plant class and Driver
"""

from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import PolyHash

hashmap = PolyHash()
hashmap.Primo_Polynomial()
tasks = MinHeap(24)

def Plant_Create():
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        print("¿Cómo se llama el parámetro " + str(i+1) + "? ")
        nameParameter = input()
        print("¿Cada cuántas horas se lleva a cabo ", nameParameter + "? ")
        frequencyParameter = int(input())
        parameter_1 = Parameter(nameParameter, frequencyParameter)
        Plant1.pushBack(parameter_1)
        tasks.Insert(parameter_1)
    hashmap.Insert(Plant1)
    return Plant1

def Plant_Read(plant):
    print(plant.Name, "tiene", plant.length, "parámetros:")
    print("Número Nombre   Frecuencia   Próxima acción")
    var = plant.head
    i = 0
    while var != None:
        x = var.key #Parámetro
        print(i,"    ",x.Name, "  ", x.Frequency, "  ", x.Next)
        var = var.next
        i += 1
    print(" ")

def Plant_Update(plant):
    print("\n¿Qué quiere hacer?",
        "\n Cambiar el nombre de", plant.Name, "(0)",
        "\n Editar parámetros (1)",
        "\n No hacer cambios (2)")
    ans = int(input())
    if ans == 0:
        hashmap.Remove(plant.Name)
        plant.Name = input("Escribe el nuevo nombre de la planta")
        hashmap.Insert(plant.Name)
    elif ans == 1:
        Plant_Read(plant)
        par_number = int(input("¿Cuál es el número del parámetro que desea actualizar? "))
        parameter_1 = plant.get(par_number).key
        print("Parámetro", par_number,
              "\n Nombre, Frecuencia, Próxima Acción \n ",
              parameter_1.Name, parameter_1.Frequency, "   ", parameter_1.Next,
              "¿Qué desea hacer?",
              "\n Eliminar parámetro (0)"
              "\n Editar parámetro (1)",
              "\n Nada (4)")
        ans_1 = int(input())
        if ans_1 == 0:
            plant.remove(par_number)
        elif ans_1 == 1:
            oldf = parameter_1.Frequency()
            oldn = parameter_1.Next()
            parameter_1.Name = input("Nombre: ")
            parameter_1.Frequency = input("Frecuencia: ")
            parameter_1.Next = input("Próxima acción: ")
            #Cambiar prioridad minheap
            if oldn != parameter_1.Next:
                x = tasks.H.index(parameter_1)
                tasks.ChangePriority(oldn, x)
            elif oldf != parameter_1.Frequency:
                p = oldn + parameter_1.Frequency - oldf
                x = tasks.H.index(parameter_1)
                tasks.ChangePriority(p, x) 
            
def Plant_Delete(plant):
    hashmap.Remove(plant.Name)
    var = plant.head
    while var != None:
        tasks.Remove(var.key.Next)
        var = var.next

#------>

plant_1 = Plant_Create()
Plant_Update(plant_1)