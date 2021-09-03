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

    
class Person(LinkedList):
    def __init__(self):
        super().__init__()
    def Create(self,plant):
        self.pushBack(plant)
    
    def Read(self,s):
      try:
        a = self.Search(s)
        print ("La planta con nombre", s, "y parámetros: ")
        planta = self.get(a).key
        for i in range(planta.len()):
          print(str(i+1)+")", planta.get(i).key.get(0).key)
        # Imprimir parámetros bien Person.get(a).keyself.get(a).key.printList(True)
      except:
        print("Planta no registrada")
  
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
              planta.get(parametro-1).key.get(0).key = nombre
            else:
              print("Inserte nueva frecuencia de realizacion")
              frecuencia = int(input())
              planta.get(parametro-1).key.get(1).key = frecuencia
        
    def Search(self, s):
        ran = self.len()
        plantTem = self.head
        for i in range(ran):
          if (s == plantTem.key.Name):
            return i
          plantTem = plantTem.next
    
    def Delete(self, n):
        for i in range(self.len()):
          if self.get(i).key.Name == n:
            self.remove(i)
            break
          else:
            ("Esa planta no esta registrada")
        print('planta eliminada')
       
