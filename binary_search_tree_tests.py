import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_it(self):
        bst = BinarySearchTree()

        #empty tree stuff
        self.assertFalse(bst.search(10)) 
        self.assertTrue(bst.is_empty())
        self.assertIsNone(bst.find_max())
        self.assertIsNone(bst.find_min())
        self.assertIsNone(bst.tree_height())
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])

        #fill it 
        self.assertIsNone(bst.insert(10, "root"))
        bst.insert(9, "left1")
        self.assertFalse(bst.is_empty())
        bst.insert(11, "right1")
        bst.insert(8, "left2")
        bst.insert(9.5, "leftright")
        bst.insert(10.5, "rightleft")
        bst.insert(12, "right2")
        bst.insert(-18)
        bst.insert(9.75, "leftright2")
        bst.insert(9.6, "leftright2left")
        
        #test search 
        self.assertTrue(bst.search(11))
        self.assertTrue(bst.search(-18))
        self.assertFalse(bst.search(10.7))
        self.assertTrue(bst.search(9.6))
        self.assertTrue(bst.search(9.75))
        self.assertTrue(bst.search(10.5))
        self.assertTrue(bst.search(12))
        self.assertFalse(bst.search(14))
        self.assertFalse(bst.search(-19))

        #test min and max 
        self.assertEqual(bst.find_min(),(-18, None))
        self.assertEqual(bst.find_max(), (12, "right2")) 

        #test tree height 
        self.assertEqual(bst.tree_height(), 4)

        #tests inorder postorder and level order 
        self.assertEqual(bst.preorder_list(), [10,9,8,-18,9.5,9.75,9.6,11,10.5,12])
        self.assertEqual(bst.inorder_list(), [-18,8,9,9.5,9.6,9.75,10,10.5,11,12])
        self.assertEqual(bst.level_order_list(), [10,9,11,8,9.5,10.5,12,-18,9.75,9.6])
        
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue1(self):
        q=Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertIsNone(q.enqueue(10))
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(),10)
        self.assertTrue(q.is_empty())
    
    def test_queue2(self):
        '''stress tests the queue by repeatedly filling and emptying it with tests along the way to ensure proper function'''
        q=Queue(3)
        #testing indexError when empty
        with self.assertRaises(IndexError):
            q.dequeue()
        
        #fill list
        for num in range(3):
            self.assertIsNone(q.enqueue(num))
        
        #test is_full, size, and is_empty on a full list 
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(),3)

        #testing indexError when full 
        with self.assertRaises(IndexError):
            q.enqueue(3)

        #dequeues and enqueues again a few times to make sure it works properly 
        self.assertEqual(q.dequeue(),0)
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 2)
        self.assertIsNone(q.enqueue(4))
        self.assertEqual(q.size(), 3)
        self.assertTrue(q.is_full())
        with self.assertRaises(IndexError):
            q.enqueue(None)
        
        #completely empty list and refill it with checks along the way
        self.assertEqual(q.dequeue(),1)
        self.assertEqual(q.dequeue(),2)
        self.assertEqual(q.dequeue(),4)
        with self.assertRaises(IndexError):
            q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(),0)
        self.assertFalse(q.is_full())

    def test_double_queues(self):
        '''tests methods when 2 lists are created together'''
        q1 = Queue(4)
        q2 = Queue(3)
        self.assertIsNone(q1.enqueue(2))
        self.assertTrue(q2.is_empty())
        self.assertFalse(q1.is_empty())
        
    #capcity zero 
    def test_zero_queue(self):
        '''tests queue of capacity zero'''
        q = Queue(0)
        self.assertTrue(q.is_full())
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.enqueue(1)
        with self.assertRaises(IndexError):
            q.dequeue()



if __name__ == '__main__': 
    unittest.main()
