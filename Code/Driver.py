import module1
import module2
import time
"""     Integrantes:
    Maria Sol Botello Leon 
    Juan David Yara Cancelada 
    Johhan Steven Maldonado Benavides
    Camilo Apraez
    David Santiago Miranda Martinez
"""


person1 = module1.Person([])

colaNotif = {}
def Usuario_Nueva_Planta():
    for i in range(ans):
        print("Hola, vamos a indexar una nueva planta")
        namePlant = input("¿Cómo se llama la nueva planta? ")
        numParam = int(input("¿Cuántos parámetros tiene la nueva planta? "))
        Plant1 = module1.Plant() #Va a guardar todos los parámetros de la planta
        
        for i in range (numParam):
            nameParam = input("¿Cómo se llama el parámetro " + str(i) + "? ")
            frequencyParam = int(input("¿Cada cuántas horas se lleva a cabo " + nameParam + "? "))
            lastParam = int(input("¿Cuándo fue la última vez que se llevó a cabo " + nameParam +"? "))
            paramTem = module1.LinkedList()
            paramTem.pushBack(nameParam)
            paramTem.pushBack(frequencyParam)
            paramTem.pushBack(lastParam)
            paramTem.pushBack(frequencyParam <= lastParam)
            paramTem.pushBack(False)
            
            Plant1.pushBack(paramTem)
            
        
        person1.Create(plant1)
        

def Usuario_Nueva_Planta1():
    for i in range(ans):
        print("Hola, vamos a indexar una nueva planta")
    
        namePlant = input("¿Cómo se llama la nueva planta? ")
        numParam = int(input("Cuántos parámetros tiene la nueva planta? "))
        paramPlant = [] #Va a guardar todos los parámetros de la planta
        
        #Guarda cada parámetro
        for i in range (numParam):
            nameParam = input("Cómo se llama el parámetro " + str(i) + "? ")
            frequencyParam = int(input("Cada cuántas horas se lleva a cabo " + nameParam + "? "))
            lastParam = int(input("Cuándo fue la última vez que se llevó a cabo " + nameParam +"? "))
            
            #Lo que antes era: name, frequencyWatering, lastWatering, needWatering, doneWatering
            paramPlant.append( [nameParam, frequencyParam, lastParam, frequencyParam <= lastParam, False])
        
        plant1 = module1.Plant(namePlant,numParam, paramPlant)
        person1.Create(plant1)
        


ans = int(input("¿Cuántas plantas quieres añadir? "))
Usuario_Nueva_Planta()
    
####---------> Interacción paso de tiempo rápido

for hour in range(24):
    print(hour)
    ran = person1.len() #Si hay 1000 plantas es costoso calcular len() cada vez
    change = int(input("¿Quieres cambiar algo? (0) no (1) sí \n"))
    if (change == 1):
        boolChange = False
        print("¿Qué quiere hacer? \n",
           " Crear nueva planta (c) \n" 
           " Actualizar planta existente (a) \n",
           " Eliminar planta existente (e)\n",
           " Leer planta existente (l)")
        an = input()
        if (an == 'c'): 
            Usuario_Nueva_Planta()
        elif(an == 'a'):
            ak = input("¿Cómo se llama la planta que quieres actualizar?: ")
            person1.Update(ak)
        elif(an == 'e'):
            ak = input("¿Cómo se llama la planta que quieres eliminar?: ")
            person1.Delete(ak)
        elif(an == 'l'):
            ak = input("¿Cómo se llama la planta que quieres leer?: ")
            person1.Read(ak)
        else: 
            print("No se entendió la respuesta, sigue el código")
    for j in range(ran):
        for i in range(person1.plantArray[j].numberParam):
            if(person1.plantArray[j].param[i][3]): #Cada parámetro de cada planta
                n = int(input(str(person1.plantArray[j].param[i][0])+" a " + 
                              person1.plantArray[j].name + 
                              ": Lo hago despues (0) Ya lo hice (1):"))
                if n==1: person1.plantArray[j].param[i][4] = True
            person1.plantArray[j].updateParameteri(i)
    time.sleep(1)
    # Pasa un segundo que contamos como una hora