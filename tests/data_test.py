import unittest

import sys
import os
from datetime import datetime

# fmt: off
CURRENT_PATH = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_PATH)
sys.path.append(ROOT_DIR)

from src.data_container import DataContainer
# fmt: on


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.data = DataContainer(os.path.join(CURRENT_PATH, 'data_test.csv'))

    def test_search_by_school_desc(self):
        self.assertEqual(self.data.search_by_school_desc(
            'onh'), [])

        self.assertEqual(self.data.search_by_school_desc(
            'tew'), [{'PARID': '0980B00120000000', 'SCHOOLDESC': 'Gateway'}])

    def test_search_by_pair_id(self):
        self.assertEqual(self.data.search_by_pair_id('123458'), '{}')

    def test_get_sale_summary(self):
        self.assertEqual(self.data.get_sale_summary(), '{"VALID SALE": 11}')

    def test_write(self):
        date = datetime.now()
        contents = 'Hello World'

        path = os.path.join(CURRENT_PATH, 'data_test.csv')
        self.data.write(contents, CURRENT_PATH, date=date)

        file_path = os.path.join(
            CURRENT_PATH, f'results-{date.isoformat()}.txt')
        with open(file_path, mode='r') as file:
            self.assertEqual(file.readline(), contents)
        os.remove(file_path)

        unknown_path = os.path.join(CURRENT_PATH, 'unknown', 'data_test.csv')
        self.data.write(contents, unknown_path, date=date)

        with self.assertRaises(FileNotFoundError):
            file_path = os.path.join(
                unknown_path, f"results-{date.isoformat()}.txt")
            with open(file_path, mode='r') as file:
                file.readline()


if __name__ == '__main__':
    unittest.main()
