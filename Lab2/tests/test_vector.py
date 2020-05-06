import unittest
from tasks.vector import Vector


class TestVector(unittest.TestCase):

    def test_add(self):
        first = Vector(3, 2, 1)
        second = Vector(3, 6, 2)
        self.assertEqual(first + second, Vector(6, 8, 3))

    def test_sub(self):
        first = Vector(3, 2)
        second = Vector(5, 2)
        self.assertEqual(first - second, Vector(-2, 0))

    def test_mul_const(self):
        vector = Vector(4, 3, 1)
        self.assertEqual(vector * 10, Vector(40, 30, 10))

    def test_mul_vect(self):
        first = Vector(7, 5, 9, 6)
        second = Vector(3, -5, 1, 5)
        self.assertEqual(first * second, Vector(21, -25, 9, 30))

    def test_len(self):
        vector = Vector(-4, -1, 0)
        self.assertEqual(len(vector), 3)

    def test_equal(self):
        self.assertEqual(Vector(-1, 5, 2, 10), Vector(-1, 5, 2, 10))

    def test_index(self):
        vector = Vector(2, 5, -10, 5)
        self.assertEqual(vector[2], -10)

    def test_not_function(self):
        self.assertEqual(Vector(1, 2, 3) * Vector(2, 3), 'Different dimensions!')


if __name__ == '__main__':
    unittest.main()
