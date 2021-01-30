#_______________ 3.3 Tape Equilibrum ___________
import unittest
import random

#_________ Method 1 ___________

import unittest

def solution(A):

    """
    Codility Grading: Task score = 69%, Correctness =57%, Performance = 83%
    
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
    :param A: non-empty list of integers
    :return: an integer - the index value where the smallest difference occurs
    
    """

    N = len(A)
    N_max = 100000
    
    if not isinstance(A, list):
        raise TypeError("The array must be a list")
        
    if (N < 2) or (N > N_max):
        raise ValueError("Length of the array is an integer within the range [2, 100,000]")
    
    for item in A:
        if not isinstance(item, int):
            raise TypeError("Elements in input must be an integer")
            
    for element in A:
       if not -1000 <= element <= 1000:
           raise ValueError("Each element of array A is an integer within the range [−1000, 1000]")
           
    
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif


#print(solution([3, 1, 2, 4, 3]))        
        
        
class TestTapeEquilibrum2(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)
        
    def test_non_int(self):
        self.assertRaises(TypeError, solution, [3,8,9,7,6,'t'])
        
    def test_small_n(self):
        self.assertRaises(ValueError, solution, [1])
    
    def test_big_elem(self):
        self.assertRaises(ValueError, solution, [3,8,9,7,6,1001])
  
        
if __name__ == '__main__':
    unittest.main()



#_________ Method 2 ________
def solution(A):

    """
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
    :param A: non-empty list of integers
    :return: an integer - the index value where the smallest difference occurs
    
    Explanation: you don’t need to test every index in the array, going up to the middle 
    element is enough because after it, you’re just swapping the right and the left elements.
    And abs(left – right) is the same as abs(right – left).
    """

    N = len(A)
    N_max = 100000
    
    if not isinstance(A, list):
        raise TypeError("The array must be a list")
        
    if (N < 2) or (N > N_max):
        raise ValueError("Length of the array is an integer within the range [2, 100,000]")
    
    for item in A:
        if not isinstance(item, int):
            raise TypeError("Elements in input must be an integer")
            
    for element in A:
       if not -1000 <= element <= 1000:
           raise ValueError("Each element of array A is an integer within the range [−1000, 1000]")
           
    
    left = A[0]
    right = sum(A[1:])
    min_diff = abs(left-right)
    
    for index in range(1, (len(A) // 2) + 1 ):
        left += A[index]
        right -= A[index]
        min_diff = min(min_diff, abs(left-right))
        
    return min_diff 


#print(solution([3, 1, 2, 4, 3]))        
        
        
class TestTapeEquilibru(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)
        
    def test_non_int(self):
        self.assertRaises(TypeError, solution, [3,8,9,7,6,'t'])
        
    def test_small_n(self):
        self.assertRaises(ValueError, solution, [1])
    
    def test_big_elem(self):
        self.assertRaises(ValueError, solution, [3,8,9,7,6,1001])
  
        
if __name__ == '__main__':
    unittest.main()
   





