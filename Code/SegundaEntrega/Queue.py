# -*- coding: utf-8 -*-
"""
Queue
"""
from linkedlist import LinkedList

class Queue(LinkedList):
    
    def __init__(self):
        super().__init__()
        
    def Enqueue(self, value):
        self.pushBack(value)
        
    def Dequeue(self):
        self.remove(0)