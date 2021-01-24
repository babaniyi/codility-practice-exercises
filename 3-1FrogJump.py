#____________________ 3. FrogJump _____________
import unittest

import unittest

maxint = 1000000000
minint = 1

def solution(X, Y, D):
    # write your code in Python 3.6
    
    if not isinstance(X, int):
        raise TypeError("Position X must be an integer")

    if not isinstance(Y, int):
        raise TypeError("Destination Position Y must be an integer")
    
    if not isinstance(D, int):
        raise TypeError("Fixed Distance D must be an integer")

    if (X < minint) or (X > maxint):
        raise ValueError("X must be within the range [1..1,000,000,000]")

    if (Y < minint) or (Y > maxint):
        raise ValueError("Y must be within the range [1..1,000,000,000]")
    
    if (D < minint) or (D > maxint):
        raise ValueError("D must be within the range [1..1,000,000,000]")

    if X <= Y:
        quot = (Y - X) // D
        rem = (Y - X) % D
        if rem == 0:
            return quot
        else:
            return quot + 1
    else:
        return ValueError("X, Y must satisfy X <= Y")



class TestFrogJump(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution(10, 85, 30), 3)

    def test_one(self):
        self.assertEqual(solution(0, 10, 1), 10)

    def test_big_steps(self):
        self.assertEqual(solution(0, 10, 20), 1)

    def test_even_steps(self):
        self.assertEqual(solution(10, 100, 10), 9)

    def test_equal_steps(self):
        self.assertEqual(solution(10, 10, 10), 0)

    def test_odd_steps(self):
        self.assertEqual(solution(9, 29, 10), 2)

if __name__ == '__main__':
    unittest.main()
