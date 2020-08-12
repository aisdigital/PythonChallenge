import unittest
import shutil
import os
import src.writer as writer

OUTPUT_PATH = './tests/output'

class TestWriter(unittest.TestCase):

    def test_write_file(self):
        content = 'The quick brown fox jumps over the lazy dog'
        path = writer.wirte_to_file(OUTPUT_PATH, content)

        with open(path, 'r') as fp:
            self.assertEqual(fp.read(), content)

    def test_write_file_create_folders(self):
        if os.path.exists(f'{OUTPUT_PATH}/temp'):
            shutil.rmtree(f'{OUTPUT_PATH}/temp')

        content = 'abc'
        path = writer.wirte_to_file(f'{OUTPUT_PATH}/temp/p1/p2/p3', content)

        with open(path, 'r') as fp:
            self.assertEqual(fp.read(), content)
