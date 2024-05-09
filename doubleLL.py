class Node:
    def __init__(self,value):
        self.value = value;
        self.previous = None;
        self.next = None;

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value);
        self.head = new_node;
        self.tail = self.head;
        self.length = 1;

    def append(self, value):
    
        new_node = Node(value);
        if self.head is None:
            self.head = new_node;
            self.tail = new_node;
            self.length = 1;
            return True;
        else:
            self.tail.next = new_node;
            new_node.previous = self.tail;
            self.tail = new_node;
            self.length += 1;
        return True;

    def pop(self):
        if self.head is None:
            return None;

        temp = self.tail;
        if self.length == 1:
            self.head = None;
            self.tail = None;
        else:
            self.tail = temp.previous;
            self.tail.next = None;
            temp.previous = None;
        self.length -= 1;
        return temp;
    
    def print_list(self):
        temp = self.head;
        while temp is not None:
            print(temp.value);
            temp = temp.next;

    def prepend(self, value):
        new_node = Node(value);
        if self.length == 0:
            self.head = new_node;
            self.tail = new_node;
            self.length = 1;
            return True;
        self.head.previous = new_node;
        new_node.next = self.head;
        self.head = new_node;
        self.length += 1;
        return True;

    def pop_first(self):
        if self.length == 0:
            return None;
        else:
            temp = self.head;
            if self.length == 1:
                self.head = None;
                self.tail = None;
            else:
                self.head = temp.next;
                temp.next = None;
                self.head.previous = None;
            self.length -=1;
            return temp;

    def get(self, index):
        if index < 0 or index >= self.length:
            return None;
        #checking the location of the index will cut the access time up to half the time
        if index > self.length/2:
            temp = self.tail;
            loop = self.length-1 - index;
            for _ in range(loop):
                temp = temp.previous;
        else:
            temp = self.head        
            for _ in range(index):
                temp = temp.next;
        return temp;

    def set_value(self, index, value):
        temp = self.get(index);
        if temp == None:
            return False;
        else:
            temp.value = value;
            return True;

    def insert(self, index, value):
        if index == self.length:
            return self.append(value);
        if index == 0:
            return self.prepend(value);
        temp = self.get(index -1);
        if temp == None:
            return False;

        
        new_node = Node(value);
        temp.next.previous = new_node;
        new_node.next = temp.next;
        temp.next = new_node;
        self.length += 1;
        return True;

    def remove(self, index):
        temp = self.get(index)
        if temp == None:
            return None;
        if index == 0:
            return self.pop_first();
        if index == self.length -1:
            return self.pop();

        temp.previous.next = temp.next
        temp.next.previous = temp.previous;
        temp.previous = None;
        temp.next = None;
        self.length -= 1;
        return temp;

    def swap_first_last(self):
        if self.length == 0 or self.length == 1:
            return;
        temp = self.head.value;
        self.head.value = self.tail.value;
        self.tail.value = temp;

    def reverse(self):
        #check whether the list is empty or has only one element
        if self.length == 0 or self.length == 1:
            return;

        #initial parameters
        current = self.head; 
        tail = current; #caputure the initial head, since it will become the tail
        previous = None; 
        
        while current is not None:
            #each node will have to have it's previous and next pointers flipped
            next = current.next
            current.next = previous; # the previous node will now become the next node 
            current.previous = next; # the next node will become the previous
            previous = current; #Move the pointer forward in the list
            current = next; 
            

        self.head = previous;
        self.tail = tail;
        return True;


dll = DoubleLinkedList(1);
dll.append(2);
dll.append(3);
dll.append(4);
dll.append(5);
dll.append(6);
dll.append(7);
dll.append(8);
dll.reverse();

# print(dll.remove(5).value)
print ("----------------");
dll.print_list()