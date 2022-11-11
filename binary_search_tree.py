from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST

    def is_empty(self): 
        # returns True if tree is empty, else False

    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
    
    def search_helper(self, node, key):
        
    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method

    def insert_helper(self, node, key, data):


    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method

    def find_min_helper(self, node):

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method

    def find_max_helper(self, node):

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method


    def tree_height_helper(self, node):
        

    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method


    def inorder_list_helper(self, node):

    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method


    def preorder_list_helper(self, node):

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000) # Don't change this!

