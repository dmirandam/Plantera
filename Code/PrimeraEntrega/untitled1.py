class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.previous = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        #Apuntador de cola

    def add(self, index,key):
        #Añade en el index pedido
        var = self.head 
        newNode = Node(key)
        for i in range(index-1):
            var = var.next
         
        if(index == 0): 
            if(self.head):
                newNode.next = self.head
                self.head.previous = newNode
            self.head = newNode
            
        else:
            if(var == None):
                print("Index out of range")
                return
            if(var.next):
                newNode.next = var.next
                var.next.previous = newNode
            newNode.previous = var
            var.next = newNode
            
    def get(self, index):
        #Devuelve valor en index
        val = self.head
        for i in range(index):
            if(val == None): return
            val = val.next
        return val.key
    
    def remove(self,index):
        #Quita elemento en el index
        var = self.head 
        for i in range(index):
            var = var.next
        tem = var
        if(tem.previous):
            var.previous.next = var.next
        if(tem.next):
            var.next.previous = tem.previous
        if(index == 0): 
            self.head = self.head.next
        return tem.key

    def pushBack(self, key): 
      #Añade al comienzo
        NewNode = Node(key)
        
        if(self.head is None):
            self.head = NewNode
        else:
            val = self.head
            while(val.next is not None):
                val = val.next

            val.next = NewNode
            NewNode.previous = val
    def Leng(self):
      val = self.head
      if self.head is None:
          return 0
      else:
          suma = 0
          while val.next:
            suma += 1
            val = val.next
          suma += 1
          return suma
        
        
    def printList(self):
        if(self.head == None):
            return ''
        val = self.head
        while(val.next):
            print(val.key)
            val = val.next
        print(val.key, end = '')
#--------------Driver

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
    def pop(self):
        return self.remove(0)
    def push(self, key):
        self.pushBack( key)
    def peek(self):
        return self.get(0).key
    

def insertz1(arr, stack): #Llamar append y guardar undo
    ar1 = arr[0] #Aclarar append
    ar2 = len(arr[2:len(arr)]) #Cantidad de caracteres nuevos
    guardar = ar1 + str(ar2)#Undo
    stack.push(guardar)#Undo
    return(arr[2:len(arr)])

def insertz2(arr,op, stack): #Llamar Delete y guardar undo
    ar1 = arr[0]
    ar2 = arr[2:len(arr)]#Cantidad de caracteres quitados
    guardar = ar1 + op[ len(op)-int(ar2):len(op) ]#Caracteres quitados
    stack.push(guardar)#Undo
    return(arr[2:len(arr)])#Devuelve pedazo de string

n = int(input())
arr = "" #String que se está editando
stack = Stack() #Últimos cambios
prints = LinkedList() #Por imprimir

#----
for i in range(n):
    op = input()
    if op[0] == "1":
      operation = insertz1(op, stack)
      arr = arr + operation
    elif op[0] == "2":
      operation = insertz2(op, arr, stack)
      arr = arr[0:len(arr)-int(operation)]
    elif op[0] == "3":
      prints.pushBack(arr[int(op[2:])-1])
    else:
      operation = stack.pop()
      if operation[0] == "1":
        arr = arr[0:len(arr)-int(operation[1:])]
      else:
        arr = arr + operation[1:]

prints.printList()
