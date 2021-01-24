import unittest
import random


#N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(A, K):
    if not isinstance(A, list):
        raise TypeError("Input must be of type list")
    
    if not isinstance(K, int):
        raise TypeError("K rotation must be an integer")
        
    N = len(A)
    
    if (N < 0) or (N >100):
        raise ValueError("Number of items in array must be within [0, 100]")
        
    if  (K < 0) or (K >100): 
        raise ValueError("Number of K rotations must be within [0, 100]")
        
    for item in A:
        if not isinstance(item, int):
            raise ValueError("Items in array must be an integer")
    
    for item in A:
        if (item < -1000) or (item > 1000):
            raise ValueError("Element of array must be an integer within the range [−1000, 1000]")
            
    if A:
        for _ in range(K):
            popped = A.pop()
            A.insert(0, popped)
        return A
    
    else:
        return A
    

class TestCyclicRotation(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(solution([], 3), [])
        
    def test_one(self):
        self.assertEqual(solution([5], 4), [5])
    
    def test_zero(self):
        self.assertEqual(solution([3,8,9,7,6], 0), [3,8,9,7,6])
        
    def test_big_K(self):
        self.assertRaises(ValueError, solution, [3,8,9,7,6], 102)
        
    def test_non_int_in_array(self):
        self.assertRaises(ValueError,solution, [3,8,9,7,'g'], 2)
        
    def test_non_int_K(self):
        self.assertRaises(TypeError, solution, [3,8,9,7,6], 't')
        
    def test_example1(self):
        self.assertEqual(solution([3,8,9,7,6], 3), [9,7,6,3,8])
        
    def test_example2(self):
        self.assertEqual(solution([1,2,3,4], 4), [1,2,3,4])
        
    def test_example3(self):
        self.assertEqual(solution([0,0,0], 1), [0,0,0])


if __name__ == '__main__':
    unittest.main()

