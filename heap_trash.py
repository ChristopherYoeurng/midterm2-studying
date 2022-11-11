
class MaxHeap:
    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = [None]*capacity
        self.num_items = 1  
        self.capacity = capacity 

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False 
        
        self.heap[self.num_items] = item 
        self.perc_up(self.num_items)
        self.num_items +=1 
        return True 

        

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None 
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None 
        maxVal = self.heap[1]
        self.heap[1] = None #added this for the edge case of 1 item tree
        self.heap[1] = self.heap[self.num_items-1]
        self.perc_down(1)
        self.num_items -= 1
        return maxVal 



    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        lst = []
        for i in range(1,self.num_items):
            lst.append(self.heap[i])
        return lst 



    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        self.heap = [None]*max(self.capacity, len(alist)+1)
        for i in range(len(alist)):
            self.heap[i+1] = alist[i]

        lastParent = len(alist)//2

        while lastParent>=1:
            self.perc_down(lastParent)
            lastParent = (lastParent*2 - 2) //2
        self.num_items = len(alist)+1


    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.num_items==1


    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.num_items >= self.capacity
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity-1
    
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items -1

        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        if self.heap[i*2] is None : 
            return 
        if self.heap[i*2+1] is None:
            if self.heap[i*2]<self.heap[i]:
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                return self.perc_down(i*2)
            return 
        if self.heap[i*2]<self.heap[i] and self.heap[i*2+1] < self.heap[i]:
            return 
        if self.heap[i*2] < self.heap[i*2+1]:
            self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
            return self.perc_down(i*2)
        self.heap[i], self.heap[i*2+1] = self.heap[i*2+1], self.heap[i]
        return self.perc_down(i*2+1)
        

        
    def perc_up(self, i): 
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        #base case 1: at top already 
        if i ==0:
            return 
        if self.heap[i] <= self.heap[i//2]:
            return 
        self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]        
        return self.perc_up(i//2)

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        alist[:] = self.contents()



