"""
Plant class and Driver
"""
import time
from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import PolyHash
from linkedlist import LinkedList

hashmap = PolyHash()
hashmap.Primo_Polynomial()
tasks = MinHeap(24)
l_list = LinkedList()

def Parameter_Create(Plant1):
    print("¿Cómo se llama el parámetro? ")
    nameParameter = input()
    print("¿Cada cuántas horas se lleva a cabo ", nameParameter + "? ")
    frequencyParameter = int(input())
    parameter_1 = Parameter(nameParameter, 
                            frequencyParameter,
                            frequencyParameter + hour, 
                            Plant1)
    Plant1.pushBack(parameter_1)
    tasks.Insert(parameter_1)

def Plant_Create():
    global hashmap
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        Parameter_Create(Plant1)
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
        hashmap.Remove(plant)
        plant.Name = input("Escribe el nuevo nombre de la planta")
        hashmap.Insert(plant)
    elif ans == 1:
        Plant_Read(plant)
        par_number = int(input("¿Cuál es el número del parámetro que desea actualizar? "))
        parameter_1 = plant.get(par_number).key
        print("Parámetro", par_number,
              "\n Nombre, Frecuencia, Próxima Acción \n ",
              parameter_1.Name, parameter_1.Frequency, "   ", parameter_1.Next,
              "\n¿Qué desea hacer?",
              "\n Eliminar parámetro (0)"
              "\n Editar parámetro (1)",
              "\n Añadir parámetro (2)"
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
                tasks.ChangePriority(oldn, tasks.H.index(parameter_1))
            elif oldf != parameter_1.Frequency:
                tasks.ChangePriority(oldn + parameter_1.Frequency - oldf, 
                                     tasks.H.index(parameter_1)) 
        elif ans_1 == 2:
            Parameter_Create(plant)
            
            
def Plant_Delete(plant):
    hashmap.Remove(plant)
    var = plant.head
    while var != None:
        tasks.Remove(var.key.Next)
        var = var.next
        
def Task_Update():
    if tasks.Min() == None: return
    if tasks.Min().Next <= hour: 
        l_list.pushBack(tasks.ExtractMin())
        Task_Update()
    else: pass

def Notif_Read():
    var = l_list.head
    for i in range(l_list.length):
        print(i, var.key.Plant, var.key.Name)
        var = var.next

def Notif_Update():
    if l_list.length == 0:
        pass
    else:
        Notif_Read()
        print("¿Realizó alguna tarea?",
              "\n (1) Sí",
              "\n (2) No")
        ans = int(input())
        if ans == 1:
            print("¿Cuál es el número de la tarea que llevo a cabo")
            num = int(input())
            a = l_list.remove(num)
            a.Next = a.Frequency + time.time() - time.start()
            tasks.Insert(a)
            Notif_Update()
        
def Person_Read():
    for i in range(len(hashmap.Hashtable)):
        if hashmap.Hashtable[i] == 0:
            continue
        else:
            var = hashmap.Hashtable[i].head
            while var != None:
                print(var.key.Name)
                var = var.next
    

#------> while temporal

hour = -1
while True:
    hour += 1
    print("Hora:", hour)
    a = input("Quiere editar alguna planta?: \n (1) Sí \n (2) No \n")
    if a == "1":
        print("Seleccione que quiere hacer",
                  "\n (1) Eliminar Planta",
                  "\n (2) Agregar planta",
                  "\n (3) Modificar planta",
                  "\n (4) nada xd \n")
        b = input()
        if b == "1": #EliminarPlanta
            if hashmap.elementos == 1:
                print("No hay plantas guardadas")
            else:
                Person_Read()
                print("Escriba el nombre de la planta a eliminar")
                c = input()
                plant_node = hashmap.Find(c)
                if plant_node == None:
                    print("Planta no existe")
                else:
                    Plant_Delete(plant_node.key)
                #print(hashmap.Hashtable)
        elif b == "2":#CrearPlanta
            Plant_Create()
        elif b == "3":#UpdatePlanta
            if hashmap.elementos == 1:
                print("No hay plantas guardadas")
            else:
                Person_Read()
                print("Escriba el nombre de la planta a editar")
                c = input()
                plant_node = hashmap.Find(c)
                if plant_node == None:
                    print("Planta no existe")
                else:
                    Plant_Update(plant_node.key)
#comparacion
    Task_Update()
    Notif_Update()