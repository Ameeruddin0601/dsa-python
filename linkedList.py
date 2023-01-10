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

myList = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)

myList.head = first
first.next = second
second.next =third

#myList.print_list()
myList.push_begin(5)
myList.push_end(40)
myList.print_list()

#push node at any position of LL
#delete node at any position of LL