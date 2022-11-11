from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key 
        self.data = data 
        self.left = left 
        self.right = right 
        

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None 

    def is_empty(self): 
        # returns True if tree is empty, else False
        return self.root is None 


    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.search_helper(self.root, key)
    

    def search_helper(self, node, key):
        if node is None:
            return False
        if node.key == key: 
            return True 
        if node.key< key:
            return self.search_helper(node.right)
        return self.search_helper(node.left)

    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.insert_helper(self.root, key, data)

    def insert_helper(self, node, key, data):
        if key == node.key:
            node = TreeNode(key, data)
        if key > node.key:
            if node.right is None: 
                node.right = TreeNode(key, data)
                return
            return self.insert_helper(node.right, key, data)
        if key < node.key:
            if node.left is None: 
                node.left = TreeNode(key,data)
                return 
            return self.insert_helper(node.left, key, data)
        


    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_min_helper(self.root)

    def find_min_helper(self, node):
        if node.left is None:
            return node 
        return self.find_min_helper(node.left)

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)

    def find_max_helper(self, node):
        if node.right is None:
            return node 
        return self.find_max_helper(node.right)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.tree_height_helper(self.root)


    def tree_height_helper(self, node):
        if node is None: 
            return 0
        return 1 + max(self.tree_height_helper(node.left), self.tree_height_helper(node.right))
        

    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.inorder_list_helper(self.root)


    def inorder_list_helper(self, node):
        if node is None: 
            return [] 
        return self.inorder_list_helper(node.left) + [node] + self.inorder_list_helper(node.right)
    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.preorder_list_helper(self.root)

    def preorder_list_helper(self, node):
        if node is None: 
            return [] 
        return [node]+self.inorder_list_helper(node.left) + self.inorder_list_helper(node.right)
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000) # Don't change this!
        lst = []
        node = self.root
        i = 0
        while node is not None: 
            q.enqueue(node)
            if i %2 ==0:
                node = node.left 
            else: 
                node = node.right 
        while not q.is_empty():
            lst.append(q.dequeue())
        return lst


