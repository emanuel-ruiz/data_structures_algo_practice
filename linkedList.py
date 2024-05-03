'''
    LINKED LIST 
    - Head 
    - Tail - Udemy Video adds it. Book didn't

    -Add to Tail = O(1)
        - To remove the Tail = O(n)
    
    -Add to Head = O(1)
    -Remove to Head = O(1)
    
    -Add and Remove from within List = O(n)

    -Search value or index = O(n)
'''

class Node:
    def __init__(self,value):
        self.value = value;
        self.next = None;

class LinkedList:
    def __init__(self,value):
        new_node = Node(value);
        self.head = new_node;
        self.tail = new_node;
        self.length = 1;

    def print_list(self):
        temp = self.head;
        while temp is not None:
            print(temp.value);
            temp = temp.next;
    
    def append(self, value):
        new_node = Node(value);
        if self.head == None:
            self.head = new_node;
            self.tail = new_node;
        else:
            self.tail.next = new_node;
            self.tail = new_node;
        
        self.length += 1;
        return True;
    
    
    def pop(self):
        if self.length == 0:
            return None;
        if self.length == 1:
            temp = self.head
            self.head = None; 
            self.tail = None;
            self.length = 0;
            return temp;
        else:
            temp = self.head;
            while temp is not self.tail:
                if temp.next == self.tail:
                    rTemp = self.tail;
                    temp.next = None;
                    self.tail = temp;
                    self.length -=1;
                    return rTemp;
                else: 
                    temp = temp.next;
    
    def prepend(self, value):
        new_node = Node(value);
        if self.length == 0:
            self.head = new_node; 
            self.tail = new_node;
            self.length += 1;
        else:
            new_node.next = self.head;
            self.head = new_node;
            self.length +=1;
        return True;
    
    def pop_first(self):
        if self.length == 0:
            return None;
        if self.length == 1:
            temp = self.head;
            self.head = None; 
            self.tail = None;
            self.length -= 1;
            return temp;
        else:
            temp = self.head
            self.head = self.head.next;
            self.length -= 1;
            temp.next = None; #make sure that the returned node no longer is attached to the linked list
            return temp;

    def get(self, index):
        if index < 0 or index > self.length-1:
            return None;
        else:
            temp = self.head;
            count = 0;
            while temp is not None:
                if count == index:
                    return temp;
                else:
                    temp = temp.next;
                    count += 1;
    
    def set_value(self, index, value):
        temp = self.get(index);
        if temp is not None:
            temp.value = value;
            return True;
        return False;

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False;
        if index == 0:
            self.prepend(value);
            return True;
        elif index == self.length:
            self.append(value);
            return True;
        else:
            new_node = Node(value);
            temp = self.get(index -1);
            new_node.next = temp.next;
            temp.next = new_node;
            self.length += 1;
            return True;

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None;
        if index == 0:
            return self.pop_first();
        if index == self.length-1:
            return self.pop();
        
        temp = self.get(index-1);
        rTemp = temp.next
        temp.next = rTemp.next;
        rTemp.next = None
        self.length -=1;
        return rTemp
    
    def reverse(self):
        if self.length == 0 or self.length == 1:
            return True
        # nList = LinkedList(self.head.value);
        # temp = self.head.next
        # for _ in range(self.length-1):
        #     nList.prepend(temp.value);
        #     temp = temp.next;
        # self.head = nList.head

        temp = self.head;
        self.head = self.tail;
        self.tail = temp;
        after = temp.next;
        before = None;
        for _ in range(self.length):
            after = temp.next;
            temp.next = before;
            before = temp
            temp = after
        return True;
            





            


llist = LinkedList(34);
llist.append(3);
llist.append(35);
llist.prepend(45);


llist.set_value(2, 69);
llist.insert(3, 44)
llist.print_list();
print('******************');
llist.reverse();
llist.print_list();






