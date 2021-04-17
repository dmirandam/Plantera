import module1
import time


dem = int(input("Quieres un DEMO (0) o quieres comenzar de una (1)? "))
print (dem, type(dem))
if dem == 0:
    print("Creamos una nueva planta llamada Rose que se riega cada 2 horas y se regó hace 3 horas")
    rose = module1.Plant("Rose",4,3)
elif dem == 1:
    print("Hola, vamos a indexar una nueva planta")
    nameNP = input("¿Cómo se llama la nueva planta? ")

    #numberNP = input("Cuántos parámetros tiene la nueva planta? ")#Se implementa después
    param1NP = input("Cómo se llama el parámetro 1? ")#Se implementa después

    frequencyNP = input("Cada cuántas horas quieres llevar a cabo " + param1NP)
    lastNP = input("Cuándo fue la última vez que se llevó a cabo" + param1NP)
    rose = module1.Plant(nameNP,frequencyNP,lastNP)

####---------> Interacción paso de tiempo rápido
time0 = time.time()
print(time.time()-time0)
print("need ","last ","frequency")
while(time.time()-time0 < 24): #Los segundos en un día
    
    #print(rose.needWatering,rose.lastWatering, rose.frequencyWatering)
    #Implementando lo de Miranda, después se implementa la pila
    #Se debe hacer lo mismo con cada parámetro
    if(rose.needWatering):
        n = int(input("Regar a Rose: Lo hago despues (0) Ya lo hice (1):"))
        if n==1: rose.doneWatering = True
        #
    rose.updateLastWatering()
    time.sleep(1)
    # Pasa un segundo que contamos como una hora
