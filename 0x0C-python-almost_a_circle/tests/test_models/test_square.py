#!/usr/bin/python3
"""Unittest for Square
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """

    def test_1_simple(self):
        """Simple tests that the basic program must pass
        """
        s1 = Square(1)
        s2 = Square(3)
        s3 = Square(5, 6, 7, 44)
        s4 = Square(8, 9, 9)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s2.id, 10)
        self.assertEqual(s3.id, 44)
        self.assertEqual(s4.id, 11)

    def test_2_adv(self):
        """Edge cases that must be accounted for
        """
        s5 = Square(3, 3, 3, "string ID")
        s6 = Square(3, 3, 3, (1, 2))
        s7 = Square(3, 3, 3, None)
        self.assertEqual(s5.id, "string ID")
        self.assertEqual(s6.id, (1, 2))
        self.assertEqual(s7.id, 12)


if __name__ == "__main__":
    unittest.main()
