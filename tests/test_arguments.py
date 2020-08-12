import unittest
import argparse
from io import StringIO
from unittest.mock import patch
from src.arguments import Arguments

class TestArguments(unittest.TestCase):

    @patch('sys.stderr', new_callable=StringIO)
    def test_mutually_exclusive_parameters(self, mock_stderr):
        with self.assertRaises(SystemExit):
            Arguments(['--sale-summary --find-pair-id 0617D00178000000'])

        with self.assertRaises(SystemExit):
            Arguments(['--sale-summary --filter-school-desc abc'])

        with self.assertRaises(SystemExit):
            Arguments(['--find-pair-id 0617D00178000000 --filter-school-desc abc'])
