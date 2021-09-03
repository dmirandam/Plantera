class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, index,key):
        #Añade en el index pedido
        var = self.head 
        newNode = Node(key)
        for i in range(index-1):
            var = var.next
        if(index == 0): 
            if(self.head):
                newNode.next = self.head
            self.head = newNode
        else:
            if(var == None):
                print("Index out of range")
                return
            elif(var.next):
                newNode.next = var.next
            else:
                self.tail = newNode
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
        
        if index == 0: 
            removeVar = self.head
            self.head = self.head.next
        else:
            var = self.head 
            for i in range(index-1):
                var = var.next
            removeVar = var.next
            if removeVar.next == None:
                self.tail = removeVar
            var.next = removeVar.next
        return removeVar.key

    def pushFront(self, key): 
        #Añade al comienzo
        NewNode = Node(key)
        NewNode.next = self.head
        self.head = NewNode
        if(self.tail is None):
            self.tail = self.head
        
    
    def pushBack(self, key):
        newNode = Node(key)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def printList( self):
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
        self.pushFront(key)
    def peek(self):
        return self.get(0).key
    
class TextEditor():
    def __init__(self):
        super().__init__() 
        self.toPrint = LinkedList()
        self.toUndo = Stack()
        
    def Append(self, strText, strAdd):
        self.toUndo.push("1"+ str(len(strAdd))+strAdd)
        return strText+strAdd
    
    def Delete(self, strText, n):#Delete last n letters
        strDeleted = strText[-int(n):]
        self.toUndo.push("2" + str(n) + strDeleted)
        return strText[:-int(n)]
    
    def Print(self,text,n):
        self.toPrint.pushBack(text[int(n)-1])
        
    def Undo(self, strText):
        strChange = self.toUndo.pop()
        if strChange[0]== '1': #revert append
            return strText[:-int(strChange[1])]
        if strChange[0]== '2':
            return strText + strChange[2:]
#-----> Driver

n = int(input())
text = ""
editor = TextEditor()

for i in range(n):
    op = input()
    if op[0] == "1": 
        text = editor.Append(text, op[2:])
    elif op[0] == "2": 
        text = editor.Delete(text, op[2:])
    elif op[0] == "3": 
        editor.Print(text, op[2:])
    elif op[0] == "4": 
        text = editor.Undo(text)
    #print(text, " ")
    #editor.toPrint.printList()
    #print(" ")
    #editor.toUndo.printList()
    #print("\n")
editor.toPrint.printList()
'''
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1

8
1 abcde
1 fg
3 6
2 5
4
3 7
4
3 4	
'''