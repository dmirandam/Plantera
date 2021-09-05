# -*- coding: utf-8 -*-
"""
MinHeap
"""
#import sys, 
import numpy
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
        self.size += 1
        self.H[self.size] = p
        self.SiftUp(self.size)
        
    def ExtractMin(self):
        if self.H[1] == None : return None
        result = self.H[1].Next
        self.H[1] = self.H[self.size]
        self.size -= 1
        self.SiftDown(1)
        return result
    
    def Min(self):
        return self.H[1]
    
    def Remove(self, i):
        if self.H[1] == None : return None
        self.H[i].Next = 0
        self.SiftUp(i)
        self.ExtractMin()
        
    def ChangePriority(self, i, p):
        if self.H[i] == None : return None
        oldp = self.H[i].Next
        self.H[i].Next = p
        if p > oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

