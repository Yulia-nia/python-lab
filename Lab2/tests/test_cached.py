import unittest
import time
from tasks.cached import cached_func, fact


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

        self.assertEqual(15, result_1)
        self.assertEqual(48, result_2)

    def test_time(self):
        start = time.time()
        cached_func(fact(200))
        first_timer = time.time() - start

        start = time.time()
        cached_func(fact(200))
        second_timer = time.time() - start

        assert second_timer < first_timer


if __name__ == '__main__':
    unittest.main()
