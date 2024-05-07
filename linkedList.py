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
    
    #Coding Exercise 14 Find Middle Node;
    # With a length class member
    def middle_node(self):
        if self.length == 0:
            return None;
        if self.length == 1:
            return self.head;
        middle = self.length //2;
        return self.get(middle);

    #without a length class member
    def find_middle_node(self):
        temp = self.head;
        temp2 = self.head;
        if temp == None:
            return None;
        if temp.next == None:
            return temp;
        while temp2 is not None and temp2.next is not None:
            temp2 = temp2.next.next;
            temp = temp.next
        return temp;

    def has_loop(self):  #use the Floyd's cycle finding algorithm
        if self.length == 0 or self.length == 1:
            return False;
    
        slow = self.head;
        fast = self.head;
        #if there is a loop, eventually they will meet 
        while fast is not None and fast.next is not None:
            fast = fast.next.next;
            slow = slow.next;

            if slow == fast:
                return True;

        return False;

    """This is my initial pass of the algorithm
        After reviewing the solution I see that it was unneccessary to create so many dummy nodes
        In total I would only need 4
        psuedo code

        create two dummy nodes with value 0 //this will be the start of the list
        create two more nodes and set them equal to the first

        //no need for counters
        set temp to head
        traverse with while loop
            if less than x 
                less than node.next = temp
                less node = temp
            else
                more than node.next = temp
                more node = temp

            temp = temp.next;


        set less and more nodes.next = None

        less.next = more head node.next
        self.head = less head node.next

            
        
    """
    def partition_list(self, x):
        #if there is only one node or the list is empty return without changing the linked list
        if self.head == self.tail or self.head == None:
            return; 


        temp = self.head;
        #capture the starting nodes of the partitions
        hLess = None; #head of less than 
        hMore = None; #head of more than
        less = None;     
        lTail = None; # tail of last less item
        mTail = None;
        more = None;
        lCount = 0; 
        mCount = 0;
        while temp is not None:
            if temp.value < x:
                if lCount == 0: #capture first item that is less than
                    hLess = temp; #set the head of the less than nodes
                    less = hLess; #needed to add to the less than list without forgett
                    lTail = hLess;
                    temp = temp.next;
                    lCount += 1
                else:
                    less.next = temp; 
                    less = temp;
                    lTail = less; 
                    temp = temp.next;
            else:
                if mCount == 0:
                    hMore = temp;
                    mTail = hMore;
                    more = hMore;
                    temp = temp.next;
                    mCount += 1;
                else:
                    more.next = temp;
                    more = temp;
                    mTail = more;
                    temp = temp.next;
        
        # make sure that previous links are severed
        if mTail is not None:
            mTail.next = None
        if hLess is not None:
            self.head = hLess;
            if hMore is not None:
                lTail.next = hMore;
            else:
                lTail.next = None; #prevent loop
        else:
            self.head = hMore;




def find_kth_from_end(llist, k):
    if k < 0: # bounds check
        return None;
    if llist.head == None: #check that the linked list is not empty
        return None;
    if llist.head == llist.tail and k ==1: 
        return llist.head;
    
    fast = llist.head;
    slow = llist.head;
    #traverse the linked list up to k position for the first pointer
    #This guarantees that there will be k difference between fast and slow pointers
    #if k is greater than the length of the structure then it will return none. 
    for _ in range(k):
        fast = fast.next;
        if fast == None:
            return None;
    while fast is not None:
        slow = slow.next;
        fast = fast.next;
    return slow;

def remove_duplicates(self):
    #check whether the linked list is empty or has only one element
    if self.head is None:
        return False;
    if self.head.next is None:
        return True;

    #create temp set to hold values
    temp_set = {self.head.value};
    current = self.head.next;
    previous = self.head;
    while current is not None: # searching for value in set is O(1) on average since it uses a hash
        #check if value is in the set
        if current.value in temp_set:
            #if value is already present, then the previous node will point to the next on the list
            #previous will not be updated since the following Node may also be a duplicate
            previous.next = current.next;
            current.next = None; #break the link to the duplicate Node
            current = previous.next; # update current
            self.length -=1; 
        else:
            #Node value is not present, therefore add the value to the set
            temp_set.add(current.value);
            #update previous and current
            previous = current;
            current = current.next;

    return True;


    






llist = LinkedList(34);
llist.append(33);
llist.append(13);
llist.append(8);
llist.append(7);
llist.append(2);



# llist.set_value(2, 69);

llist.print_list();
print('******************');
llist.partition_list(33);
llist.print_list();








