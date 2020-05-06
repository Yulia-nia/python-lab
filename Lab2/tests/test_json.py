import unittest
import json
import tasks.json as to_json


class TestJson(unittest.TestCase):
    def test_null(self):
        self.assertEqual(to_json.json_convert(None), json.dumps(None))

    def test_bool(self):
        self.assertEqual(to_json.json_convert(True), json.dumps(True))
        self.assertEqual(to_json.json_convert(False), json.dumps(False))

    def test_int(self):
        self.assertEqual(to_json.json_convert(3), json.dumps(3))

    def test_float(self):
        self.assertEqual(to_json.json_convert(3.8), json.dumps(3.8))

    def test_string(self):
        self.assertEqual(to_json.json_convert("Hello word!"), json.dumps("Hello word!"))

    def test_list(self):
        current_list = [12, 13, 15.5, "Hello!", True]
        self.assertEqual(to_json.json_convert(current_list), json.dumps(current_list))

    def test_tuple(self):
        current_tuple = (4, 6, 8)
        self.assertEqual(to_json.json_convert(current_tuple), json.dumps(current_tuple))

    def test_dict(self):
        current_dict = {5: "cucumber", 8: False, 10: [2, 4, 5]}
        self.assertEqual(to_json.json_convert(current_dict), json.dumps(current_dict))


if __name__ == '__main__':
    unittest.main()
