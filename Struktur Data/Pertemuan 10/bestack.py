# Implementasi Stack dengan Linked List

# 1 membuat kelas node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # Methode cek isEmpty
    def is_Empty(self):
        return self.top is None

    # Methode push
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Methode pop
    def pop(self):
        if self.is_Empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    # Methode peek / Top
    def peek(self):
        if self.is_Empty():
            return None
        return self.top.data

    # Methode Display / cetak tumpukan
    def Display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next


MyStack = Stack()
print(MyStack.is_Empty())
MyStack.push(10)
MyStack.push(20)
MyStack.push(30)
MyStack.Display()
print(MyStack.pop())
print(MyStack.peek())
print(MyStack.is_Empty())
MyStack.Display()
