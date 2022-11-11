
class MaxHeap:
    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = [None]*(capacity+1)
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False 
        self.num_items +=1
        self.heap[self.num_items] = item 
        self.perc_up(self.num_items)
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
        max = self.heap[1]
        self.heap[1] = self.heap[self.num_items]
        self.heap[self.num_items] = None 
        self.num_items -=1
        self.perc_down(1)
        return max 




    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        lst = []
        for item in self.heap:
            if item is not None:
                lst.append(item)
        return lst 




    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if len(alist)>self.get_capacity():
            self.heap = [None] + alist[:]
        else:
            self.heap[:] = [None]*(self.get_capacity()+1)
        for i in range(len(alist)):
            self.heap[i+1] = alist[i]
        self.num_items = len(alist)
        i = len(alist) // 2
        while (i > 0):
            self.perc_down(i)
            i = i - 1




    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.num_items==0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.num_items == self.get_capacity()

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return len(self.heap)-1

    
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items

    def maxChild(self,i):
        if i*2+1 > self.num_items:
            return i*2
        if self.heap[i*2] > self.heap[i*2+1]:
            return i*2
        return i*2+1

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i*2<= self.num_items:
            max_child = self.maxChild(i)
            if self.heap[i] < self.heap[max_child]:
                self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            i = max_child

        

        
    def perc_up(self, i): 
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i//2>0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //=2


    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        for i in range (self.get_size()):
            alist[i] = self.dequeue()
        alist[:] = alist[::-1]
        

        




