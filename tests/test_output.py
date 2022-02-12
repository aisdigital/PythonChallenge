import glob
import os
import pytest
from src.output import dump_result_txt


def test_dump_result_txt():
    """Test if dump_result_txt() can create a file successfully"""
    number_of_files_in_directory = len(os.listdir())
    # create new file with empty data for testing
    dump_result_txt([], 'test_')
    new_number_of_files_in_directory = len(os.listdir())
    # remove generated test file
    for filename in glob.glob("test_*"):
        os.remove(filename) 
    assert new_number_of_files_in_directory == number_of_files_in_directory + 1


def test_dump_result_txt_invalid_file_name():
    """Test if dump_result_txt() can raise a invalid file name exception successfully"""
    # try to call dump_result_txt with and invalid directory as an argument
    with pytest.raises(SystemExit) as pytest_wrapped_e:
           dump_result_txt([], '?????')
    assert pytest_wrapped_e.type == SystemExit
    # 4 is the defined system exit value for this error
    assert pytest_wrapped_e.value.code == 4
    