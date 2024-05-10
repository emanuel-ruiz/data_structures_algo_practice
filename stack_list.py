class Stack:
    def __init__(self):
        self.stack_list = [];
    
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i]);
    
    def is_empty(self):
        return len(self.stack_list) == 0;

    def push(self, value):
        self.stack_list.append(value);

    def pop(self):
        if self.is_empty():
            return None;
        else:
            return self.stack_list.pop();

    def peek(self):
        if self.is_empty():
            return None;
        return self.stack_list[-1];

def sort_stack(input_list):
    if input_list.is_empty() == True:
        return True;
    sorted_stack = Stack();
    sorted_stack.push(input_list.pop());

    while input_list.is_empty() == False:
        temp = input_list.pop();
        print(sorted_stack.peek())
        #we want to put the values from lowest to highest in the sorted_stack list
        #so when we put it back to the original list it will sorted_stack
        while not sorted_stack.is_empty() == False and sorted_stack.peek() > temp:
            input_list.push(sorted_stack.pop());
        sorted_stack.push(temp);
    
    while sorted_stack.is_empty() == False:
        input_list.push(sorted_stack.pop());


    if stack_list.is_empty() == True:
        return True;
    
    sort_stack = Stack();
    sort_stack.push(stack_list.pop());
    
    while stack_list.is_empty() == False:
        temp = stack_list.pop();
        
        while sort_stack.is_empty() == False and sort_stack.peek() > temp:
            stack_list.push(sort_stack.pop())
        sort_stack.push(temp)
        
    while sort_stack.is_empty() == False:
        stack_list.push(sort_stack.pop());
 

myStack = Stack();
myStack.push(4);
myStack.push(5);
myStack.push(1);
myStack.push(23);

sort_stack(myStack);
myStack.print_stack();