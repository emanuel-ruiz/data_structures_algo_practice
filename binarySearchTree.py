class Node: 
    def __init__(self, value):
        self.value = value;
        self.left = None;
        self.right = None;

class BinarySearchTree:
    def __init__(self):
        self.root = None;
    
    def insert(self, value):
        new_node = Node(value);
        if self.root is None:
            self.root = new_node;
            return True;
        temp = self.root;
        while(True):
            
            if new_node.value == temp.value:
                return False;
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node;
                    return True;
                else:
                    temp = temp.left;
            else:
                if temp.right == None:
                    temp.right = new_node;
                    return True;
                else:
                    temp = temp.right;

    def contains(self, value):
        temp = self.root;
        while temp is not None:
            if temp.value == value:
                return True;
            if value < temp.value:
                temp = temp.left;
            else:
                temp = temp.right;
        return False;


bst = BinarySearchTree();
bst.insert(23);
bst.insert(3);
bst.insert(45);

print(bst.root.value);
print(bst.root.left.value);
print(bst.root.right.value);