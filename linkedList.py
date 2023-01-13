class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp!=None:
                print(temp.data, end = " > ")
                temp = temp.next
    
    #push node at start of Linked List
    def push_begin(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    #push node at end of Linked List
    def push_end(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = NewNode
    
    def push_afterNode(self,data,x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            temp = temp.next
        
        if temp is None:
            print("Node is not present in a Linked List")
        else:
            NewNode = Node(data)
            NewNode.next = temp.next
            temp.next = NewNode

    def push_beforeNode(self,data,x):
        NewNode = Node(data)
        if self.head is None:
            print("Linked List is empty") 
            return
        if self.head.data == x: #if the node is to pushed before first node
            NewNode.next = self.head
            self.head = NewNode            
        else: #finding previous node
            temp = self.head
            while temp.next is not None:
                if temp.next.data == x:
                    break
                temp = temp.next
            if temp.next is None:
                print("Node is not present in a Linked List")
            else:
                NewNode.next = temp.next
                temp.next = NewNode

    def insert_empty(self,data):
        if self.head is None:
            NewNode = Node(data)
            self.head = NewNode
        else:
            print("Linked List Is Not Empty")

    #delete the first Node from LL
    def del_first(self):
        if self.head is None:
            print("LL is already empty")
        else:
            self.head = self.head.next

    def del_last(self):
        if self.head is None:
            print("LL is already empty")
        elif self.head.next is None:
            self.head = None     
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def del_node(self,data):
        if self.head is None:
            print("LL is already empty")       
        elif data==self.head.data:
            self.del_first()        
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == data:
                    break
                temp = temp.next
            if temp.next is None:
                print("Node is not present in a Linked List")
            else:
                temp.next = temp.next.next               

myList = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)

myList.head = first
first.next = second
second.next =third

#myList.print_list()
# myList.insert_empty(25)
myList.push_begin(5)
myList.push_end(40)
myList.push_afterNode(15,10)
myList.push_beforeNode(35,400)
myList.del_first()
myList.del_last()
myList.del_node(45)
myList.print_list()

#push node at any position of LL
#delete node at any position of LL