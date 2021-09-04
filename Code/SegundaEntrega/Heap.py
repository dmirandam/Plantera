# -*- coding: utf-8 -*-
"""
MinHeap
"""
import sys, numpy
from Plant_Parameter import Parameter

#--------> Classes

class MinHeap:
    
    #Aqui .Next se refiere a el .Next de la clase Parameter
    def __init__(self, maxSize):#Falta hacerlo dinámico
        self.size = 0
        self.maxSize = maxSize
        self.H = numpy.empty(maxSize, dtype=object)
        
    def Parent(self, i):
        return i//2
    
    def LeftChild(self, i):
        return 2*i
    
    def RightChild(self, i):
        return 2*i +1
    
    def SiftUp(self, i):
        while i>1 and self.H[i].Next < self.H[self.Parent(i)].Next:
            temp = self.H[i] #Swap
            self.H[i] = self.H[self.Parent(i)] 
            self.H[self.Parent(i)] = temp
            i = self.Parent(i)
            
    def SiftDown(self, i):
        minIndex = i
        l = self.LeftChild(i)
        r = self.RightChild(i)
        if l <= self.size and self.H[l].Next < self.H[minIndex].Next:
            minIndex = l
        if r <= self.size and self.H[r].Next < self.H[minIndex].Next:
            minIndex = r
        if i != minIndex: #Swap
            temp = self.H[i]
            self.H[i] = self.H[minIndex] 
            self.H[minIndex] = temp
            self.SiftDown(minIndex)
    
    def Insert(self, p):
        if self.size == self.maxSize:
            return #
        self.size += 1
        self.H[self.size] = p
        self.SiftUp(self.size)
        
    def ExtractMin(self):
        result = self.H[1].Next
        self.H[1].Next = self.H[self.size].Next
        self.size -= 1
        self.SiftDown(1)
        return result
    
    def Remove(self, i):
        self.H[i].Next = 0
        self.SiftUp(i)
        self.ExtractMin()
        
    def ChangePriority(self, i, p):
        oldp = self.H[i].Next
        self.H[i].Next = p
        if p > oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

#--------> Driver

maxi = MinHeap(24)#sys.getsizeof(int()))
for i in [12,10,8,6,4,2,0]:

    parameter_i = Parameter(str(i),i)
    maxi.Insert(parameter_i)

maxi.ExtractMin()
maxi.ExtractMin()
maxi.Remove(6)