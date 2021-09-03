
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.previous = None
class LinkedList: #Clase constructura para una lista simplemente enlazada
    def __init__(self):
        self.head = None
    
    def add(self, index, key): #añadir nodo en posicion especifica 
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

    def get(self, index): #
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

    def pushBack(self, key): #añade un elemento en la ultima posición
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
      val = self.head #puntero
      num = 0
      while(val != None):
        num += 1
        val = val.next
      return num

class Plant(LinkedList): #define la clase planta con sus distintos parámetros 
    def __init__(self, n, np):
        super().__init__()
        self.Name = n  
        self.NumberParam = np
        #self.pushBack(p)  #parametros
        #falta cola
