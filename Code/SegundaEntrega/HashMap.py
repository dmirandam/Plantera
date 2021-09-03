import math
import random
from LinkedList import LinkedList, Plant, Node
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