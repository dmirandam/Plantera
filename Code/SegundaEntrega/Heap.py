
import sys
#--------> Classes
class MinHeap:
    def __init__(self, maxSize):
        self.size = 0
        self.maxSize = maxSize
        self.H = [0] * (self.maxSize + 1)
        
    def Parent(self, i):
        return i//2
    
    def LeftChild(self, i):
        return 2*i
    
    def RightChild(self, i):
        return 2*i +1
    
    def SiftUp(self, i):
        while i>1 and self.H[i] < self.H[self.Parent(i)]:#Change
            temp = self.H[i]
            self.H[i] = self.H[self.Parent(i)] 
            self.H[self.Parent(i)] = temp
            i = self.Parent(i)
            
    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        r = self.RightChild(i)
        if l <= self.size and self.H[l] < self.H[maxIndex]:
            maxIndex = l
        if r <= self.size and self.H[r] < self.H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            temp = self.H[i]
            self.H[i] = self.H[maxIndex] 
            self.H[maxIndex] = temp
            self.SiftDown(maxIndex)
    
    def Insert(self, p):
        if self.size == self.maxSize:
            return #error
        self.size += 1
        self.H[self.size] = p
        self.SiftUp(self.size)
        
    def ExtractMin(self):
        result = self.H[1]
        self.H[1] = self.H[self.size]
        self.size -= 1
        self.SiftDown(1)
        return result
    
    def Remove(self, i):
        self.H[i] = 0
        self.SiftUp(i)
        self.ExtractMin()
        
    def ChangePriority(self, i, p):
        oldp = self.H[i]
        self.H[i] = p
        if p > oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

#--------> Driver

maxi = MinHeap(24)#sys.getsizeof(int()))
for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
    maxi.Insert(i)

maxi.ExtractMin()
maxi.ExtractMin()
maxi.Remove(6)