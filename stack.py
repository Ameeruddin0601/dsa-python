#Stack implementation
stack=[]
def push():
    if len(stack)==len_stack:
        print("Stack is full")
    else:
        element = input("Enter the element: ")
        stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is already empty.")
    else:
        element = stack.pop()
        print("Element popped: ",element)
        print(stack)
len_stack=int(input("Limit of stack: "))
while True:  
    user_input = int(input("Enter your choice: \n 1. Push\n 2.Pop\n 3.Quit\n ->"))
    if user_input==1:
        push()
    elif user_input==2:
        pop()
    elif user_input==3:
        break
    else:
        print("Enter the correct choice!")

