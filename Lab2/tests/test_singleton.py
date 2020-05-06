import unittest
from tasks.singleton import Singleton


class SomeClass(metaclass=Singleton):
    pass


class MyTestCase(unittest.TestCase):

    def test_address(self):
        obj1 = SomeClass()
        obj2 = SomeClass()
        self.assertEqual(id(obj1), id(obj2))


if __name__ == '__main__':
    unittest.main()
