import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    
    def test_selection(self):
        nums = [5,4,3,2,1]
        python_sort= sorted(nums)
        comps = selection_sort(nums)
        self.assertListEqual(nums,python_sort)
        self.assertEqual(comps, 10)

    def test_insertion(self):
        nums = [5,2,1,8,6,12]
        python_sort = sorted(nums)
        comps = insertion_sort(nums)
        self.assertListEqual(nums, python_sort)
        self.assertEqual(comps, 7)
        

if __name__ == '__main__': 
    unittest.main()
