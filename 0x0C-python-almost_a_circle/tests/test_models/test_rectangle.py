#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """

    def test_1_simple(self):
        """Simple tests that the basic program must pass
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(5, 6, 0, 0, 44)
        r4 = Rectangle(7, 8)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r3.id, 44)
        self.assertEqual(r4.id, 7)

    def test_2_adv(self):
        """Edge cases that must be accounted for
        """
        r5 = Rectangle(3, 3, 3, 3, "string ID")
        r6 = Rectangle(3, 3, 3, 3, (1, 2))
        r7 = Rectangle(3, 3, 3, 3, None)
        self.assertEqual(r5.id, "string ID")
        self.assertEqual(r6.id, (1, 2))
        self.assertEqual(r7.id, 8)


if __name__ == "__main__":
    unittest.main()
