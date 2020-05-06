import unittest

from tasks.cached import cached_func


class TestCached(unittest.TestCase):
    def test(self):
        @cached_func
        def mul(first, second):
            return first * second

        first_value = 3
        second_value = 5
        result_1 = mul(first_value, second_value)

        first_value = 6
        second_value = 8
        result_2 = mul(first_value, second_value)

        self.assertIs(15, result_1)
        self.assertIs(48, result_2)


if __name__ == '__main__':
    unittest.main()
