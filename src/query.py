import json


def search_by_school_desc(data, school_desc, dump_in_file):
    """Search all the entries that contains school_desc and show the PAIRID and SCHOOLDESC of each one

    Args:
        data (DataFrame): data stored in memory from CSV file
        school_desc (str): text to be searched in SCHOOLDESC column
        dump_in_file (bool): disables print in console

    Returns:
        result (DataFrame): two-dimensional data structure with labeled axes filtered by query
    """

    # obtain all entries whose SCHOOLDESC column has the school_desc argument
    result = data[data['SCHOOLDESC'].str.contains(school_desc)]
    # filter columns PARID and SCHOOLDESC from result and convert to str
    result = result.filter(items=['PARID', 'SCHOOLDESC']).to_string()
    # print on console if the dump_in_file is false
    if not dump_in_file:
        print("\nRESULT --filter-school-desc" + school_desc + ":")
        print(result)
    return result


def search_by_pair_id(data, pair_id, dump_in_file):
    """Find an entry by PARID and output the full entry in JSON format on the screen

    Args:
        data (DataFrame): data stored in memory from CSV file
        pair_id (int): value to be searched in PARID column
        dump_in_file (bool): disables print in console

    Returns:
        result (str): full entry with correspondent pair_id in JSON format
    """

    # obtain the entry with correspondent pair_id argument
    result = data[data['PARID'] == pair_id]
    # convert result to json
    result = result.to_json(orient="records")
    # load json object
    result = json.loads(result)
    # format json object
    result = json.dumps(result, indent=4)
    # print on console if the dump_in_file is false
    if not dump_in_file:
        print("\nRESULT --find-pair-id" + pair_id + ":")
        print(result)
    return result


def sale_summary(data, dump_in_file):
    """How many sales for each SALEDESC

    Args:
        data (DataFrame): data stored in memory from CSV file
        dump_in_file (bool): disables print in console

    Returns:
        result (str):
    """

    # count the ocurrency of each value present on the SALEDESC column
    result = data['SALEDESC'].value_counts()
    # convert result to json
    result = result.to_json(orient="columns")
    # load json object
    result = json.loads(result)
    # format json object
    result = json.dumps(result, indent=4)
    # print on console if the dump_in_file is false
    if not dump_in_file:
        print('\nRESULT --sale-summary:')
        print(result)
    return result
