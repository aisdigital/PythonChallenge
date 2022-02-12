import datetime
import sys


def dump_result_txt(results, directory):
    """Writes query results in a file results-{timestamp-iso}.txt

    Args:
        results (list[str]): the array of query results
        directory (str): the directory where the results file is going to be created
    """

    # iso_timestamp stores current time in ISO 8601 format compatible with Windows (without :)
    iso_timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%SZ")
    # open file in write mode
    try:
        result_file = open(directory + "results-" + iso_timestamp + ".txt", "w")
    except OSError:
        print('ERROR: Invalid file name')
        sys.exit(4)
    # write all results in the results file
    for result in results:
        result_file.write(result + "\n")
    # close the results file
    result_file.close()
