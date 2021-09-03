import random
import math

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

####################################
def esPrimo(n):
    if n <= 1:
        return False
    if math.sqrt(n).is_integer():
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def encontrar_primo():
    x = 27**6
    n = random.randint(x, x+(10**10))
    while esPrimo(n) == False:
        n += 1
    return n

class hash:
    def __init__(self):
        self.hashtable = [0]*100
        self.espacio = 100
        self.elementos = 1
        self.primo = 0
        self.polynomial = 0

    def primo_polynomial(self):
        self.primo = encontrar_primo()
        self.polynomial = random.randint(1, self.primo-1)

    def polyhash(self, string):
        hash = 0
        for i in string[::-1]:
            hash = (hash*self.polynomial+(ord(i)-96))
        return (hash%self.primo)%self.espacio
    def rehash(self):
        if self.elementos/ self.espacio > 0.5:
            self.espacio = self.espacio*2
            newhash = [0]*self.espacio
            self.primo_polynomial()
            for i in self.hashtable:
                if i == 0:
                    continue
                newhash.insert(self.polyhash(i.Name),i)
                self.elementos += 1
            self.hashtable = newhash
    def find(self, planta):
        return(self.hashtable[self.polyhash(planta.Name)])
    def insert(self, planta):
        if self.hashtable[self.polyhash(planta.Name)] == 0:
            list = LinkedList()
            list.pushBack(planta)
            self.hashtable[self.polyhash(planta.Name)] = list
            self.elementos += 1
            self.rehash()
        else:
            self.hashtable[self.polyhash(planta.Name)].pushBack(planta)
            self.elementos += 1
    def remove(self, planta):
        if self.hashtable[self.polyhash(planta.Name)].len() == 1:
            self.hashtable[self.polyhash(planta.Name)] = 0
        else:
            for i in range(self.hashtable[self.polyhash(planta.Name)].len()-1):
                if self.hashtable[self.polyhash(planta.Name)].get(i).key.Name == planta.Name:
                    self.hashtable[self.polyhash(planta.Name)].remove(i)
        self.elementos -= 1

###test

hash = hash()
hash.primo_polynomial()

planta = Plant("rosa", 0)
hash.insert(planta)
planta3 = Plant("rosa", 0)
hash.insert(planta3)
planta2 = Plant("arroz", 0)
hash.insert(planta2)
hash.remove(planta3)
hash.remove(planta2)
print(hash.hashtable)