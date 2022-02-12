import json
import pytest
from src.storage import read_and_store_CSV
from src.query import search_by_school_desc, search_by_pair_id, sale_summary


@pytest.fixture
def data():
    return read_and_store_CSV('./input/property_sales_transactions.csv')


@pytest.fixture
def school_desc_test_result():
    return '291591'


@pytest.fixture
def pair_id_test_result():
    return [{'PARID': '0028S00066000000', 'PROPERTYHOUSENUM': 3326.0, 'PROPERTYFRACTION': ' ', 'PROPERTYADDRESSDIR': None, 'PROPERTYADDRESSSTREET': 'DAWSON', 'PROPERTYADDRESSSUF': 'ST', 'PROPERTYADDRESSUNITDESC': None, 'PROPERTYUNITNO': None, 'PROPERTYCITY': 'PITTSBURGH', 'PROPERTYSTATE': 'PA', 'PROPERTYZIP': 15213.0, 'SCHOOLCODE': 47, 'SCHOOLDESC': 'Pittsburgh', 'MUNICODE': 104, 'MUNIDESC': '4th Ward - PITTSBURGH', 'RECORDDATE': '2013-04-23', 'SALEDATE': '2013-04-23', 'PRICE': 157000.0, 'DEEDBOOK': '15213', 'DEEDPAGE': '395', 'SALECODE': '0', 'SALEDESC': 'VALID SALE', 'INSTRTYP': 'DE', 'INSTRTYPDESC': 'DEED'}]


@pytest.fixture
def sale_summary_test_result():
    return {'LOVE AND AFFECTION SALE': 57041, 'QUIT CLAIM / SPECIAL WARRANTY': 40891, 'VALID SALE': 37435, 'MULTI-PARCEL SALE': 37281, 'TIME ON MARKET (INSUFF/EXCESS)': 18946, 'SALE NOT ANALYZED': 15816, 'OTHER VALID': 14677, 'OTHER INVALID SALES INDICATED': 11818, 'SHERIFF SALE': 11620, 'CORRECTIVE DEED / DUPLICATE SALE': 9682, 'OTHER': 7109, 'GOVERNMENT SALE': 5961, 'DATE OF TRANSFER (RECORD YR <> SALE YR)': 3769, 'CORPORATION TRANSFER': 3467, 'BUILDING NOT YET ASSESSED': 3255, 'NO ASSESSED VALUATION': 2549, 'CITY TREASURER SALE': 2389, 'ESTATE SALE': 2110, 'NOT APPLICABLE': 1772, 'SALE OF PREVIOUS FORECLOSURE - INVALID': 1144, 'BANK/FINANCIAL INSTITUTION': 1061, 'EXEMPT BUYER OR SELLER': 500, 'INCLUDES PERSONAL PROPERTY': 359, 'CHANGED AFTER SALE': 352, 'SHORT SALE - INVALID': 249, 'PREFERENTIAL ASMT': 195, 'COURT ORDERED SALE': 128, 'PREFERENTIAL VALID CLEAN & GREEN': 20}
    

def test_search_by_school_desc_Park(data, school_desc_test_result):
    """Test if search_by_school_desc(), using Park as an argument, can return the expected result successfully
    
    Args:
        data (TextFileReader): CSV file descriptor
        school_desc_test_result (str): number of expected entries when using Park as an argument in search_by_school_desc()
    """

    # pass dump_as_file flag to disable printing
    result = search_by_school_desc(data, 'Park', True)
    # obtain last line of df in string format, that contains the number of results found
    result = result.splitlines()[-1]
    # split last line in the first blank space to obtain the number
    assert result.split(' ')[0] == school_desc_test_result


def test_search_by_pair_id_0028S00066000000(data, pair_id_test_result):
    """Test if search_by_pair_id(), using 0028S00066000000 as an argument, can return the expected result successfully
        
    Args:
        data (TextFileReader): CSV file descriptor
        pair_id_test_result (JSON as a dict): expected JSON when using 0028S00066000000 as an argument in search_by_pair_id()
    """

    # pass dump_as_file flag to disable printing
    result = search_by_pair_id(data, '0028S00066000000', True)
    json_result = json.loads(result)
    assert json_result == pair_id_test_result


def test_sale_summary(data, sale_summary_test_result):
    """Test if sale_summary() can return the expected result successfully
        
    Args:
        data (TextFileReader): CSV file descriptor
        sale_summary_test_result (JSON as a dict): expected JSON when calling sale_summary()
    """

    # pass dump_as_file flag to disable printing
    result = sale_summary(data, True)
    json_result = json.loads(result)
    assert json_result == sale_summary_test_result
