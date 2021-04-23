import module1
import time
#Ahora se pueden manejar cuántos parámetros se quiera por planta.
#Los parámetros se guardan en una lista
#Cada paámetro es una lista que contiene a los siguientes
#    param[i] es el parámetro i
#    param[i][0] <- nombre del parámetro, nueva variable
#    param[i][1] <- frequencyWatering
#    param[i][2] <- lastWatering
#    param[i][3] <- needWatering
#    param[i][4] <- doneWatering

dem = int(input("Quieres un DEMO (0) o quieres comenzar de una (1)? "))

if dem == 0:#DEMO
    print("Creamos una nueva planta llamada Rose ",
          "con un solo parámetro: Agua 5 3")
    plant1 = module1.Plant("Rose", 2,
                           [["Agua", 5, 3, False, False],
                            ["Tierra", 5, 3, False, False]])
elif dem == 1:#Ingresar datos uno por uno
    #Me parece mejor pasar la info completa a la clase
    #Con eso se puede pasar fácilmente la info en un archivo
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
    
    
####---------> Interacción paso de tiempo rápido

for hour in range(24):
    print(hour)

    for i in range(plant1.numberParam):
        if(plant1.param[i][3]): #Cada parámetro de cada planta
            n = int(input(str(plant1.param[i][0])+" a " + plant1.name + 
                          ": Lo hago despues (0) Ya lo hice (1):"))
            if n==1: plant1.param[i][4] = True
        plant1.updateParameteri(i)
    time.sleep(1)
    # Pasa un segundo que contamos como una hora
