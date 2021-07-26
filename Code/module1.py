# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, index, key):
        var = self.head
        newNode = Node(key)
        for i in range(index - 1):
            var = var.next

        if (index == 0):
            if (self.head):
                newNode.next = self.head
                self.head.previous = newNode
            self.head = newNode

        else:
            if (var == None):
                print("Index out of range")
                return
            if (var.next):
                newNode.next = var.next
                var.next.previous = newNode
            newNode.previous = var
            var.next = newNode

    def get(self, index):
        val = self.head
        for i in range(index):
            if (val == None): return
            val = val.next
        return val

    def remove(self, index):
        var = self.head
        for i in range(index):
            if (var.next == None):
                raise IndexError
            var = var.next
        if (var == None): raise IndexError
        tem = var
        if (index == 0):
            self.head = self.head.next
        if (tem.previous):
            var.previous.next = var.next
        if (tem.next):
            var.next.previous = tem.previous

        return tem

    def pushBack(self, key):
        NewNode = Node(key)

        if (self.head is None):
            self.head = NewNode
        else:
            val = self.head
            while (val.next is not None):
                val = val.next

            val.next = NewNode
            NewNode.previous = val

    def printList(self, bool):
        if (self.head == None):
            return
        val = self.head
        out = ""
        while (val.next is not None):
            out += str(val.key) + " "
            val = val.next
        out += str(val.key)
        if (bool):
            out += " "
            print(out)
        else:
            print(out, end="")
    def len(self):
      val = self.head
      num = 0
      while(val != None):
        num += 1
        val = val.next
      return num

class Plant(LinkedList):
    def __init__(self, n, np):
        super().__init__()
        self.Name = n  
        self.NumberParam = np
        #self.pushBack(p)  #parametros
        #falta cola

    def UpdateParam(self, i):
        paramTem = self.get(i).key
        #nameParam,
        #frequencyParam
        #lastParam
        #frequencyParam <= lastParam
        #False

        if paramTem.get(4).key == False:
            if paramTem.get(1).key - 3 < paramTem.get(
                    2).key:  #Entonces sí se necesita agua
                if paramTem.get(3).key == False:
                    #self.cola[paramTem.get(0).key] = 0
                    paramTem.get(3).key = True
            paramTem.get(2).key += 1

        #Si se acaba de regar
        else:
            paramTem.get(2).key = 0
            paramTem.get(4).key = False
            paramTem.get(3).key = False

    #Notificaciones, se organizan en colas
    def notif(self):
        pass
        print("              ***NOTIFICACIONES***")
        for i in self.cola:
            if self.cola[i] == 0:
                print("debes", i, "a", self.name)
            else:
                print("debes", i, "a", self.name, "tuviste que hacerlo hace:",
                      self.cola[i], "horas")
            self.cola[i] += 1

    def Desnotif(self, a):
        pass
        for i in self.cola:
            if a == i:
                del self.cola[i]
            print("           Has hecho", a, " a", self.name)
            break
        #Si se acaba de regar
        else:
          pass
            #paramTem.get(2).key = 0
            #paramTem.get(4).key = False
            #paramTem.get(3).key = False

    #Notificaciones, se organizan en colas
    #def notif(str,num):
    
class Person(LinkedList):
    def __init__(self):
        super().__init__()
    def Create(self,plant):
        self.pushBack(plant)
    def Read(self,s):
        a = self.Search(s)
        
        print ("La planta con nombre", s, "y parámetros", self.get(a).key.printList(True))
        # Imprimir parámetros bien Person.get(a).key

    def Update(self, s):
        a = self.Search(s)
        planta = self.get(a).key
        print("¿que parametro quieres actualizar de ",  planta.Name,"?")

        for i in range(planta.len()):
          print(str(i+1)+")", planta.get(i).key.get(0).key)
          
        parametro = int(input())
        if parametro > planta.len() or parametro < 0:
          print("Parametro inexistente, no se actualizo la planta")

        else:
          print("¿Que desea cambiar? \n 1) Nombre del parametro \n 2) frecuencia de realizacion \n")
          decision = int(input())
          if decision <= 0 or decision > 2:
            print("No se entendio la respuesta, no se actualizo el parametro")

          else:
            if decision == 1:
              print("Inserte nuevo nombre del parametro:")
              nombre = input()
              print(planta.get(parametro))
              planta.get(parametro).key.get(0).key = nombre
            else:
              print("Inserte nueva frecuencia de realizacion")
              frecuencia = int(input())
              planta.get(parametro).key.get(1).key = frecuencia
        
    def Search(self, s):
        ran = self.len()
        plantTem = self.head
        for i in range(ran):
          if (s == plantTem.key.Name):
            return i
          plantTem = plantTem.next
    
    def Delete(self, n):
      if(type(n) == type(0)):
        self.remove(n)
      elif(type(n) == type("a")):
        self.remove(self.Search(n))
      else: print("Can´t delete by", type (n))
       

''''


    def Update(self, string):
        nuevo = self.Search(string)

        print("¿que parametro quieres actualizar de ",self.plantArray[nuevo].name, "?")

        for i in range(self.plantArray[nuevo].numberParam):
          print(str(i+1)+")", self.plantArray[nuevo].param[i][0])
          
        parametro = int(input())
        if parametro > self.plantArray[nuevo].numberParam or parametro < 0:
          print("Parametro inexistente, no se actualizo la planta")
        else:
          print("¿Que desea cambiar? \n 1) Nombre del parametro \n 2) frecuencia de realizacion \n")
          decision = int(input())
          if decision <= 0 or decision > 2:
            print("No se entendio la respuesta, no se actualizo el parametro")
          else:
            if decision == 1:
              print("Inserte nuevo nombre del parametro:")
              nombre = input()
              self.plantArray[nuevo].param[parametro - 1][0] = nombre
            else:
              print("Inserte nueva frecuencia de realizacion")
              frecuencia = int(input())
              self.plantArray[nuevo].param[parametro - 1][1] = frecuencia 
        #self.Delete(string)
       
        #self.Create()
    
    def Delete(self, string):
        self.plantArray.pop(self.Search(string))
    
    
        
class Person:    
    def check(self):
        print("Exists")
        
    def __init__(self,a):
        self.plantArray = a
    
#----> CRUD

    def Create(self,plant):
        self.plantArray.append(plant)
    
    #Después: CRUD respecto al index
    def Read(self, string):
        a = self.plantArray[self.Search(string)]
        print("La planta con nombre" , a.name, "y parámetros", a.param)

    def Update(self, string):#Esto queda bien? Podríamos editar un parámetro en específico o algo así
        nuevo = self.Search(string)

        print("¿que parametro quieres actualizar de ",self.plantArray[nuevo].name, "?")

        for i in range(self.plantArray[nuevo].numberParam):
          print(str(i+1)+")", self.plantArray[nuevo].param[i][0])
          
        parametro = int(input())
        if parametro > self.plantArray[nuevo].numberParam or parametro < 0:
          print("Parametro inexistente, no se actualizo la planta")
        else:
          print("¿Que desea cambiar? \n 1) Nombre del parametro \n 2) frecuencia de realizacion \n")
          decision = int(input())
          if decision <= 0 or decision > 2:
            print("No se entendio la respuesta, no se actualizo el parametro")
          else:
            if decision == 1:
              print("Inserte nuevo nombre del parametro:")
              nombre = input()
              self.plantArray[nuevo].param[parametro - 1][0] = nombre
            else:
              print("Inserte nueva frecuencia de realizacion")
              frecuencia = int(input())
              self.plantArray[nuevo].param[parametro - 1][1] = frecuencia 
        #self.Delete(string)
       
        #self.Create()
    
    def Delete(self, string):
        self.plantArray.pop(self.Search(string))
    
    def Search(self, string):#Tal vez podríamos organizar en orden alfabético
        ran = len(self.plantArray)
        for i in range(ran):
            if (string == self.plantArray[i].name):
                return i
        
'''  ''''
class Plant:

    def check(self): #Revisar si se creo algo
        print("exists")
    
    #Parametrized constructor
    def __init__(self, n, np, p):
        self.name = n
        self.numberParam = np
        #param es una lista que contiene a cada parámetro
        #Cada parámetro es una lista que contiene la info Name, frequency, last, need, done
        #Lo que antes era FrequencyWatering, lastWatering, needWatering, doneWatering
        self.param = p
        self.cola = {}


    def updateParameteri(self,i):
        #Exactamente igual a updateWatering, solo se cambiaron los nombres correspondientes
        if self.param[i][4] == False:
            if self.param[i][1]-3 < self.param[i][2]: #Entonces sí se necesita agua
                if self.param[i][3] == False:
                    self.cola[self.param[i][0]] = 0
                    self.param[i][3] = True
            self.param[i][2] += 1
        
        #Si se acaba de regar
        else: 
            self.param[i][2] = 0
            self.param[i][4] = False
            self.param[i][3] = False

    #Notificaciones, se organizan en colas
    
    def notif(self):
      print ("              ***NOTIFICACIONES***")
      for i in self.cola:
        if self.cola[i] == 0:
          print("debes", i, "a", self.name)
        else:
          print("debes",i, "a", self.name, "tuviste que hacerlo hace:", self.cola[i], "horas")
        self.cola[i] += 1
    
    def Desnotif(self,a):
      for i in self.cola:
        if a == i:
          del self.cola[i]
          print("           Has hecho",a," a",self.name)
          break


        
        #Si se acaba de regar
        else: 
            self.param[i][2] = 0
            self.param[i][4] = False
            self.param[i][3] = False

    #Notificaciones, se organizan en colas
    #def notif(str,num):

    # CRUD 
    '''
