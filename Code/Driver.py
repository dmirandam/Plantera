import module1
import module2
import time
import keyboard
#Ahora se pueden manejar cuántos parámetros se quiera por planta.
#Los parámetros se guardan en una lista


#El ejemplo literal de keyboard no funciona
#def on_triggered():
#	print("Triggered!")
#keyboard.add_hotkey('k', on_triggered)

#keyboard.is_pressed('space')
person1 = module2.Person([])

ans = int(input("¿Cuántas plantas quieres añadir? "))
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
person1.Read(namePlant)
person1.Delete(namePlant)
    
####---------> Interacción paso de tiempo rápido

for hour in range(24):
    print(hour)
    ran = len(person1.plantArray) #Si hay 1000 plantas es costoso calcular len() cada vez
    for j in range(ran):
        #if keyboard.on_press('l'):
         #   print("k was pressed")
        for i in range(person1.plantArray[j].numberParam):
            if(person1.plantArray[j].param[i][3]): #Cada parámetro de cada planta
                n = int(input(str(person1.plantArray[j].param[i][0])+" a " + 
                              person1.plantArray[j].name + 
                              ": Lo hago despues (0) Ya lo hice (1):"))
                if n==1: person1.plantArray[j].param[i][4] = True
            person1.plantArray[j].updateParameteri(i)
    time.sleep(1)
    # Pasa un segundo que contamos como una hora
