class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next

myList = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)

myList.head = first
first.next = second
second.next =third

myList.print_list()