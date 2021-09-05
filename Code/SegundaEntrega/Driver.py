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
notifications = LinkedList()

def Plant_Create():
    global hashmap
    print("Hola, vamos a indexar una nueva planta")
    namePlant = input("¿Cómo se llama la nueva planta? ")
    numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
    Plant1 = Plant(namePlant) #Va a guardar todos los parámetros de la planta
    
    for i in range (numParam):
        print("¿Cómo se llama el parámetro " + str(i+1) + "? ")
        nameParameter = input()
        print("¿Cada cuántas horas se lleva a cabo ", nameParameter + "? ")
        frequencyParameter = int(input())
        parameter_1 = Parameter(nameParameter, frequencyParameter, Plant1)
        Plant1.pushBack(parameter_1)
        tasks.Insert(parameter_1)
    hashmap.Insert(Plant1)
    print(hashmap.Hashtable)
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
    hashmap.Remove(plant)
    var = plant.head
    while var != None:
        tasks.Remove(var.key.Next)
        var = var.next
        
def Task_Update(heap, l_list):
    if heap.Min() == None: return
    if heap.Min().Next <= hour: #como acceder al primer nodo
        l_list.pushBack(heap.ExtractMin())
        Task_Update(heap, l_list)

def Notif_Read(l_list):
    var = l_list.head
    for i in range(l_list.lenght):
        print(i, var.key.Plant, var.key.Name)
        var = var.next

def Notif_Update(heap, l_list):
    if l_list.lenght == 0:
        pass
    else:
        Notif_Read(l_list)
        print("¿Realizó alguna tarea?",
              "\n (1) Sí",
              "\n (2) No")
        ans = int(input())
        if ans == 1:
            print("¿Cuál es el número de la tarea que llevo a cabo")
            num = int(input())
            a = l_list.remove(num)
            a.Next = a.Frequency + time.time() - time.start()
            heap.Insert(a)
            Notif_Update
        
def Person_Read():
    for i in range(len(hashmap.Hashtable)):
        if hashmap.Hashtable[i] == 0:
            continue
        else:
            for j in range(hashmap.Hashtable[i].length):
                print(str(j) + '. ' + hashmap.Hashtable[i].get(j).key.Name)
    

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
            if hashmap.elementList.head == None:
                print("No hay plantas guardadas")
            else:
                print("Seleccione la planta que desea eliminar")
                Person_Read()
                c = int(input())
                if hashmap.elementList.lenght <= c:
                    print("Planta no existe")
                plant_node = hashmap.elementList.get(c)
                Plant_Delete(plant_node.key)
                #print(hashmap.Hashtable)
        elif b == "2":#CrearPlanta
            Plant_Create()
        elif b == "3":#UpdatePlanta
            if hashmap.elementList.head == None:
                print("No hay plantas guardadas")
            else:
                print("Seleccione la planta que desea eliminar")
                print("Seleccione la planta que desea modificar")
                Person_Read()
                c = int(input())
                if hashmap.elementList.lenght <= c:
                    print("Planta no existe")
                plant_node = hashmap.elementList.get(c)
                Plant_Update(plant_node.key)
        
##comparacion
    Task_Update(tasks, notifications)
    Notif_Update