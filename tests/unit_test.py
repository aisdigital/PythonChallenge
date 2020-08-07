import unittest
import src.supply as sply
import src.api_back as api


class MyTest(unittest.TestCase):

    def test_transform_string(self):
        self.assertEqual(sply.transform_string("string-for-TeSt"), "STRINGFORTEST")

    def test_first_argument(self):
        self.assertEqual(sply.first_argumet("--filter-school-desc"), "SCHOOLDESC")


if __name__ == '__main__':
    unittest.main()
