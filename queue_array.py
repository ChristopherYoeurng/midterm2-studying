
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.items = [None]*capacity
        self.capacity = capacity
        self.front = 0 
        self.back = 0 
        self.num_items = 0 


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.capacity == self.num_items 


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        #adds item to back of cue 
        self.items[self.back] = item 

        #updates num_items 
        self.num_items +=1

        #if at end of array, go back to front
        if self.back == self.capacity-1:
            self.back =0
        else: 
            self.back +=1
        
            
    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        #check if empty
        if self.is_empty():
            raise IndexError 
        
        #saves the item in front
        front_item = self.items[self.front]

        #updates num_items 
        self.num_items -= 1

        #circularly changes front 
        if self.front == self.capacity-1:
            self.front = 0
        else: 
            self.front+=1

        #returns dequeued item 
        return front_item

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

