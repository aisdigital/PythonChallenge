import unittest
import filecmp
import src.reader as reader
import src.writer as writer

INPUT_TEST_FILE = './tests/input/test_property_sales_transactions.csv'
OUTPUT_PATH = './tests/output'
EXPECTED_OUTPUT_PATH = './tests/expected_output'


class TestReader(unittest.TestCase):

    def test_get_summary(self):
        result = reader.get_summary(INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_get_summary.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_find_par_id_no_matches(self):
        result = reader.find_pair_id('000000000', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_find_par_id_no_matches.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_find_par_id_one_match(self):
        result = reader.find_pair_id('0028S00066000000', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_find_par_id_one_match.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_find_par_id_multiple_matches(self):
        result = reader.find_pair_id('1105J00228000000', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_find_par_id_multiple_matches.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_filter_by_school_desc_no_matches(self):
        result = reader.filter_by_school_desc('abc', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_filter_by_school_desc_no_matches.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_filter_by_school_desc_one_match(self):
        result = reader.filter_by_school_desc('Mt Lebanon', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_filter_by_school_desc_one_match.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")

    def test_filter_by_school_desc_multiple_matches(self):
        result = reader.filter_by_school_desc('Pittsburgh', INPUT_TEST_FILE)
        result_path = writer.wirte_to_file(OUTPUT_PATH, result)
        expected_result_path = f'{EXPECTED_OUTPUT_PATH}/test_filter_by_school_desc_multiple_matches.txt'

        self.assertTrue(filecmp.cmp(result_path, expected_result_path),
                        f"The expected file ({expected_result_path}) is different from the output ({result_path})")
