class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    #traversal
    def print_dll(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" > ")
                temp = temp.next
    #reverse traversal
    def print_dll_reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            while temp is not None:
                print(temp.data, end=" > ")
                temp = temp.prev
    
    def push_empty(self,data):
        if self.head is None:
            NewNode = Node(data)
            self.head = NewNode
        else:
            print("List is not empty")

    def push_begin(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head.prev = NewNode
            self.head = NewNode
    def push_end(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head =None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next            
            NewNode.prev = temp
            temp.next = NewNode

    def push_afterNode(self,data,x):
        NewNode = Node(data)
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == x:
                    break
                temp = temp.next

            if temp is None:
                print("Node not found")
            else:
                if temp.next is None:
                    self.push_end(data)
                else:
                    NewNode.prev = temp
                    NewNode.next = temp.next
                    temp.next.prev = NewNode    
                    temp.next = NewNode

    def push_beforeNode(self,data,x):
        NewNode = Node(data)
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == x:
                    break
                temp = temp.next
            if temp is None:
                print("Node not found")
            else:
                if temp.prev is None:
                    self.push_begin(data)
                else:
                    NewNode.prev = temp.prev
                    NewNode.next = temp
                    temp.prev.next = NewNode
                    temp.prev = NewNode


    def del_first(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
            print("Node deleted. List is empty now")
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_last(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
            print("Node deleted. List is empty now")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.prev.next = None

    def del_node(self,data):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            print("Node deleted. List is empty now")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    break
                temp = temp.next
            if temp is None:
                print("Node not found")
            else:
                if temp.prev is None:
                    self.del_first()
                elif temp.next is None:
                    self.del_last()
                else:                
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = None
                    temp.prev = None

myList = DoublyLL()
first = Node(10) # myList.push_empty(10)
second = Node(20) 
third = Node(30)

myList.head = first
first.next = second
second.prev = first
second.next = third
third.prev = second


# myList.print_dll_reverse()
myList.push_begin(5)
myList.push_end(40)
myList.push_afterNode(15,10)
myList.push_afterNode(50,40)
myList.push_beforeNode(2.5,5)
myList.push_beforeNode(45,50)
myList.del_first()
myList.del_last()
myList.del_node(15)
myList.print_dll()