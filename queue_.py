#implementation of queue using list
# queue_=[]
# def enqueue():
#     element = input("Enter the element: ")
#     queue_.append(element)
#     display()
# def dequeue():
#     if not queue_:
#         print("Queue already empty")
#     else:
#         element = queue_.pop(0)
#         print("Element removed is: ", element)
#     display()
# def display():
#     print(queue_)

# while True:
#     user_input=int(input("Enter your choice: \n 1.Enqueue\n 2.Dequeu \n 3.Quit \n ->"))
#     if user_input==1:
#         enqueue()
#     elif user_input==2:
#         dequeue()
#     elif user_input==3:
#         break
#     else:
#         print("Enter correct choice.")

#implementation of queue using modules
# import collections
# queue_= collections.deque()

# def enqueue():
#     element = input("Enter the element: ")
#     queue_.appendleft(element)
#     display()
# def dequeue():
#     if not queue_:
#         print("Queue already empty")
#     else:
#         element = queue_.pop()
#         print("Element removed is: ", element)
#     display()
# def display():
#     print(queue_)

# while True:
#     user_input=int(input("Enter your choice: \n 1.Enqueue\n 2.Dequeu \n 3.Quit \n ->"))
#     if user_input==1:
#         enqueue()
#     elif user_input==2:
#         dequeue()
#     elif user_input==3:
#         break
#     else:
#         print("Enter correct choice.")

#implementation of queue using queue module
# import queue
# queue_= queue.Queue()

# def enqueue():
#     element = input("Enter the element: ")
#     queue_.put_nowait(element)
#     display()
# def dequeue():
#     if queue_.empty():
#         print("Queue already empty")
#     else:
#         element = queue_.get_nowait()
#         print("Element removed is: ", element)
#     display()
# def display():
#     print(queue_)

# while True:
#     user_input=int(input("Enter your choice: \n 1.Enqueue\n 2.Dequeu \n 3.Quit \n ->"))
#     if user_input==1:
#         enqueue()
#     elif user_input==2:
#         dequeue()
#     elif user_input==3:
#         break
#     else:
#         print("Enter correct choice.")


#priority queue
import queue
queue_= queue.PriorityQueue()

def enqueue():
    element = input("Enter the element: ")
    queue_.put_nowait(element)
    display()
def dequeue():
    if queue_.empty():
        print("Queue already empty")
    else:
        element = queue_.get_nowait()
        print("Element removed is: ", element)
    display()
def display():
    print(queue_)

while True:
    user_input=int(input("Enter your choice: \n 1.Enqueue\n 2.Dequeu \n 3.Quit \n ->"))
    if user_input==1:
        enqueue()
    elif user_input==2:
        dequeue()
    elif user_input==3:
        break
    else:
        print("Enter correct choice.")