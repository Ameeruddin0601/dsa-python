class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" > ")
                temp = temp.next
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

    def push_begin(data):
        pass
    def push_end(data):
        pass
    def push_afterNode(data):
        pass
    def push_beforeNode(data):
        pass
    def push_empty(data):
        pass

    def del_first(data):
        pass
    def del_last(data):
        pass
    def del_node(data):
        pass

myList = DoublyLL()
first = Node(10)
second = Node(20)
third = Node(30)

myList.head = first
first.next = second
second.prev = first
second.next = third
third.prev = second

myList.print_dll()
# myList.print_dll_reverse()