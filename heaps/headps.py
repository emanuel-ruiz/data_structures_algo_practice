"""Each Node's value is higher than all of it's descendants\
    Highest value will be at the top
    
    - Complete tree
        - fill from left to right, no gaps
        -height is logN
        - you can have duplicates
        - max or min heaps
        - no guarenteed order
        - Not good for searching 
        - BENEFIT : get greatest value, get smallest value instantly
        - We use a list
            - NOT nodes
        - root is index 0 or 1
        - no gaps in the list

        - Find childern: root = 1
            - Left_child = 2 * parent_index
            - right_child = 3 * parent_index + 1
        
        - finde Parent: 
            interger Division = index/2


    INSERT
        - No matter the value, we place the new value in the next available spot
        - then we bubble the value up until it is no longer greater than the parent value

    HELPER METHODS

    """
#using zero index
class MaxHeap:
    def __init__(self):
        self.heap = [];

    #Helper function to get left child index
    def _left_child(self, index):
        return 2 * index + 1;

    #Helper function to get right child index
    def _right_child(self, index):
        return 2 * index + 2;

    #Helper function to parent index
    def _parent(self, index):
        return (index-1) // 2;

    #Helper Function that swaps the values at the given index
    def _swap(self, id1, id2):
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1];
    
    #Helper function used by remove() to sink down the last element after being swapped with the root
    def _sink_down(self, index):
        
        max_in = index;
        
        while True:
            left = self._left_child(index);
            right = self._right_child(index);

            #Max value will be either the left or right child unless it is it correct location
            if left < len(self.heap) and self.heap[left] > self.heap[max_in]:
                max_in = left;

            if right < len(self.heap) and self.heap[right] > self.heap[max_in]:
                max_in = right;
    
            # value is still not in it's correct location
            if index != max_in:
                self._swap(index, max_in);
                index = max_in;
            # value is at its correct location
            else:
                return;

    # Function inserts value into it's correct location after placing it at the end
    def insert(self, val):
        self.heap.append(val);
        current = len(self.heap) - 1;
        # swap values while parent's value is less than self. 
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current));
            current = self._parent(current);

    #Function removes and returns max value
    def remove(self):
        if len(self.heap) == 0:
            return None;
        if len(self.heap) == 1:
            return self.heap.pop();

        max_val = self.heap[0];

        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_val;


myHeap = MaxHeap();
myHeap.insert(9);
myHeap.insert(89);
myHeap.insert(99);
myHeap.insert(99);
myHeap.insert(12);
myHeap.insert(71);
myHeap.insert(34);
myHeap.insert(4);

print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)