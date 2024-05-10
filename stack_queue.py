class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

class Stack:
    def __init__(self, value):
        new_node = Node(value);
        self.top = new_node;
        self.height = 1;

    def push(self,value):
        if self.height == 0:
            new_node = Node(value);
            self.top = new_node;
            self.height = 1;
        new_node = Node(value);
        new_node.next = self.top;
        self.top = new_node;
        self.height += 1;

    def pop(self):
        if self.height == 0:
            return None;
        top = self.top;
        self.top = top.next;
        top.next = None;
        self.height -=1;
        return top;

    def print_stack(self):
        if self.height == 0:
            return;

        temp = self.top;
        while temp is not None:
            print(temp.value);
            temp = temp.next;


class Queue:
    def __init__(self, value):
        new_node = Node(value);
        self.first = new_node;
        self.last = new_node;
        self.length = 1;

    def enqueue(self, value):
        new_node = Node(value);
        if self.length == 0:
            self.first = new_node;
            self.last = new_node;
            self.length = 1;
            return True;
        self.last.next = new_node;
        self.last = new_node;
        self.length += 1;
        return True;

    def dequeue(self):
        if self.length ==0:
            return None;

        first = self.first;
        if self.length ==1:
            self.first = None;
            self.last = None;
        else:
            self.first = self.first.next;
            first.next = None;
        self.length -= 1;
        return first;
    
    def print_queue(self):
        if self.length == 0:
            return;
        temp = self.first;
        while temp is not None:
            print(temp.value);
            temp = temp.next;
        return;


myStack = Stack(1);
myStack.push(3);
myStack.push(6);

myQ = Queue(56);
myQ.dequeue()
myQ.enqueue(45)
myQ.enqueue(452)
myQ.enqueue(245)
myQ.print_queue();
print("---------------")
print(myQ.dequeue().value)
myQ.dequeue()
myQ.dequeue()
myQ.dequeue()
print("---------------")
myQ.print_queue()

# while myStack.height > 0:
#     print(myStack.pop().value);
# print("-------------------------------")
# myStack.print_stack()

# myStack.print_stack()