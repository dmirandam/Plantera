"""
Plant class and Driver
"""
import time
from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import PolyHash

class Queue():
    def __init__(self):
        self.cola = []
    def pushBack(self, value):
        self.cola.insert(len(self.cola), value)
    def PopFront(self):
        self.cola.pop(0)

hashmap = PolyHash()
hashmap.Primo_Polynomial()
tasks = MinHeap(24)
notifications = Queue

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
        parameter_1 = Parameter(nameParameter, frequencyParameter)
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
def actualizar(heap, queue):
    global start_time
    if heap.H[0].Next <= start_time: #como acceder al primer nodo
        queue.PushBack(heap.ExtractMin())
        actualizar(heap, queue)
    revisar_notification(queue)

def revisar_notification(heap, queue):
    if len(queue.cola) == 0:
        pass
    else:
        for i in queue.cola:
            a = input("debes", queue.cola[0], "\n (1) ya lo hice \n (2) lo hago despues")  #se necesita un apuntador a la planta
            if a == "1":
                notif = queue.PopFront()
                heap.insert(notif)
            elif a == "2":
                notif = queue.PopFront()
                notif.Next = notif.Frequency + start_time
                queue.PushBack(notif)


#------> while temporal
planta = Plant("rosa")
hashmap.Insert(planta)
print(hashmap.Hashtable)
start_time = time.time()
while True:
    a = input("Quiere cambiar algo?: \n (1) Si \n (2) No \n")
    if a == "1":
        b = input("Seleccione que quiere modificar\n (1) Eliminar Planta \n (2)Agregar planta \n(3) Modificar planta \n (4) nada xd \n")
        if b == "1":
            print("Seleccione la planta que desea eliminar")
            l = []
            for i in range(len(hashmap.Hashtable)):
                if hashmap.Hashtable[i] == 0:
                    continue
                else:
                    for j in range(hashmap.Hashtable[i].len()):
                        l.append(hashmap.Hashtable[i].get(j).key.Name)
            for i in range(len(l)):
                print(str(i+1) + '. ' + l[i])
            c = int(input())
            hashmap.Remove(l[c-1])
            print(hashmap.Hashtable)
        elif b == "2":
            Plant_Create()
        elif b == "3":
            print("Seleccione la planta que desea modificar")
            l = []
            for i in range(len(hashmap.Hashtable)):
                if hashmap.Hashtable[i] == 0:
                    continue
                else:
                    for j in range(hashmap.Hashtable[i].len()):
                        l.append(hashmap.Hashtable[i].get(j).key.Name)
            for i in range(len(l)):
                print(str(i+1) + '. ' + l[i])
            c = input()
            if len(hashmap.Hashtable[hashmap.PolyHash(l[c])]) == 1:
                arreglar = "esto xfa" 
                #Plant_update(hashmap.Hashtable[hashmap.PolyHash(c)])
            else:
                for i in range(hashmap.Hashtable[hashmap.PolyHash(l[c])].len()-1):
                    if hashmap.Hashtable[hashmap.PolyHash(l[c])].get(i).key.Name == l[c]:
                        arreglar = "esto xfa"
                        #Plant_update(hashmap.Hashtable[hashmap.PolyHash(l[c])]).key)
        elif b == "4":
            continue
##comparacion
    actualizar(tasks, notifications)