import math
import random
from linkedlist import LinkedList, Node
from Driver import Plant

#-------------->
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

class PolyHash:
    def __init__(self):
        self.Hashtable = [0]*100
        self.espacio = 100
        self.elementos = 1
        self.primo = 0
        self.polynomial = 0

    def primo_polynomial(self):
        self.primo = encontrar_primo()
        self.polynomial = random.randint(1, self.primo-1)

    def polyHash(self, string):
        Hash = 0
        for i in string[::-1]:
            Hash = (Hash*self.polynomial + (ord(i)-96)) % self.primo
        return Hash%self.espacio
    
    def reHash(self):
        if self.elementos/ self.espacio > 0.5:
            self.espacio = self.espacio*2
            newHash = [0]*self.espacio
            self.primo_polynomial()
            for i in self.Hashtable:
                if i == 0:
                    continue
                newHash.insert(self.polyHash(i.Name),i)
                self.elementos += 1
            self.Hashtable = newHash
            
    def find(self, planta):
        return(self.Hashtable[self.polyHash(planta.Name)])
    
    def insert(self, planta):
        if self.Hashtable[self.polyHash(planta.Name)] == 0:
            list = LinkedList()
            list.pushBack(planta)
            self.Hashtable[self.polyHash(planta.Name)] = list
            self.elementos += 1
            self.reHash()
        else:
            self.Hashtable[self.polyHash(planta.Name)].pushBack(planta)
            self.elementos += 1
            
    def remove(self, planta):
        if self.Hashtable[self.polyHash(planta.Name)].len() == 1:
            self.Hashtable[self.polyHash(planta.Name)] = 0
        else:
            for i in range(self.Hashtable[self.polyHash(planta.Name)].len()-1):
                if self.Hashtable[self.polyHash(planta.Name)].get(i).key.Name == planta.Name:
                    self.Hashtable[self.polyHash(planta.Name)].remove(i)
        self.elementos -= 1

###test

Hash = PolyHash()
Hash.primo_polynomial()

planta = Plant("rosa", 0)
Hash.insert(planta)
planta3 = Plant("rosa", 0)
Hash.insert(planta3)
planta2 = Plant("arroz", 0)
Hash.insert(planta2)
Hash.remove(planta3)
Hash.remove(planta2)
print(Hash.Hashtable)