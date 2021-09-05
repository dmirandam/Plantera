import math
import random
from linkedlist import LinkedList
from Plant_Parameter import Plant
#-------------->
def EsPrimo(n):
    if n <= 1:
        return False
    if math.sqrt(n).is_integer():
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def Encontrar_Primo():
    x = 27**6
    n = random.randint(x, x+(10**10))
    while EsPrimo(n) == False:
        n += 1
    return n

class PolyHash:
    def __init__(self):
        self.Hashtable = [0]*100
        self.espacio = 100
        self.elementos = 1
        self.primo = 0
        self.polynomial = 0
        self.elementList = LinkedList()

    def Primo_Polynomial(self):
        self.primo = Encontrar_Primo()
        self.polynomial = random.randint(1, self.primo-1)

    def PolyHash(self, string):
        Hash = 0
        for i in string[::-1]:
            Hash = (Hash*self.polynomial+(ord(i)-96))%self.primo
        return Hash%self.espacio
    
    def ReHash(self):
        if self.elementos/self.espacio > 0.5:
            self.espacio = self.espacio*2
            newHash = [0]*self.espacio
            self.primo_polynomial()
            for i in self.Hashtable:
                if i == 0:
                    continue
                newHash.Insert(self.PolyHash(i.Name),i)
                self.elementos += 1
            self.Hashtable = newHash
            
    def Find(self, planta):
        return(self.Hashtable[self.PolyHash(planta.Name)])
    
    def Insert(self, planta):
        self.elementList.pushBack(planta)
        if self.Hashtable[self.PolyHash(planta.Name)] == 0:
            list = LinkedList()
            list.pushBack(planta)
            self.Hashtable[self.PolyHash(planta.Name)] = list
            self.elementos += 1
            self.ReHash()
        else:
            self.Hashtable[self.PolyHash(planta.Name)].pushBack(planta)
            self.elementos += 1
            
    def Remove(self, planta):
        if self.elementList.delete(planta) == False: return 
        if self.Hashtable[self.PolyHash(planta.Name)].length == 1:
            self.Hashtable[self.PolyHash(planta.Name)] = 0
        else:
            for i in range(self.Hashtable[self.PolyHash(planta.Name)].len()-1):
                if self.Hashtable[self.PolyHash(planta.Name)].get(i).key.Name == planta.Name:
                    self.Hashtable[self.PolyHash(planta.Name)].remove(i)
        self.elementos -= 1
"""
hashMap =  PolyHash()
hashMap.Primo_Polynomial()
planta1 = Plant("rosa")
hashMap.Insert(planta1)
print(hashMap.Remove(planta1))
print(hashMap.Hashtable)
"""