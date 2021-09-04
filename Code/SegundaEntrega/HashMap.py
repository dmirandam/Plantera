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

class Hash:
    def __init__(self):
        self.Hashtable = [0]*100
        self.espacio = 100
        self.elementos = 1
        self.primo = 0
        self.polynomial = 0

    def Primo_Polynomial(self):
        self.primo = Encontrar_Primo()
        self.polynomial = random.randint(1, self.primo-1)

    def PolyHash(self, string):
        Hash = 0
        for i in string[::-1]:
            Hash = (Hash*self.polynomial+(ord(i)-96))%self.primo
        return Hash%self.espacio
    
    def ReHash(self):
        if self.elementos/ self.espacio > 0.5:
            self.espacio = self.espacio*2
            newHash = [0]*self.espacio
            self.primo_polynomial()
            for i in self.Hashtable:
                if i == 0:
                    continue
                newHash.Insert(self.PolyHash(i.Name),i)
                self.elementos += 1
            self.Hashtable = newHash
            
    def Find(self, string):
        return(self.Hashtable[self.PolyHash(string)])
    
    def Insert(self, string):
        if self.Hashtable[self.PolyHash(string)] == 0:
            list = LinkedList()
            list.pushBack(string)
            self.Hashtable[self.PolyHash(string)] = list
            self.elementos += 1
            self.ReHash()
        else:
            self.Hashtable[self.PolyHash(string)].pushBack(string)
            self.elementos += 1
            
    def Remove(self, string):
        if self.Hashtable[self.PolyHash(string)].len() == 1:
            self.Hashtable[self.PolyHash(string)] = 0
        else:
            for i in range(self.Hashtable[self.PolyHash(string)].len()-1):
                if self.Hashtable[self.PolyHash(string)].get(i).key.Name == string:
                    self.Hashtable[self.PolyHash(string)].Remove(i)
        self.elementos -= 1
hashMap =  Hash()
hashMap.Primo_Polynomial()
planta1 = Plant("rosa", 1)
hashMap.Insert(planta1.Name)