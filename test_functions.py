import unittest
from task1_logger import hello_world
from task2_flat_iterator import FlatIterator, flat_list

class TestFunctions(unittest.TestCase):
    
    def test_flat_iterator_simple(self):
        iterator = FlatIterator([[1, 2], [3, 4]])
        self.assertEqual(list(iterator), [1, 2, 3, 4])
    
    def test_flat_iterator_diff_lengths(self):
        iterator = FlatIterator([['a', 'b'], ['c']])
        self.assertEqual(list(iterator), ['a', 'b', 'c'])
    
    def test_flat_iterator_empty(self):
        iterator = FlatIterator([[], [1], []])
        self.assertEqual(list(iterator), [1])
    
    def test_flat_list_simple(self):
        self.assertEqual(flat_list([[1,2],[3]]), [1,2,3])
    
    def test_flat_list_nested(self):
        self.assertEqual(flat_list([[1,[2,3]], [4]]), [1, 2, 3, 4])
    
    def test_flat_list_empty(self):
        self.assertEqual(flat_list([[], []]), [])
    
    def test_logger_return(self):
        result = hello_world()
        self.assertEqual(result, 'Hello World!')

if __name__ == '__main__':
    unittest.main(verbosity=2)