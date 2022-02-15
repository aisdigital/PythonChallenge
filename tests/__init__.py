# This module contains functions designed to test specific aspects of the application.
# Each test function defined here is supposed to replace the main function for the testing.
# To accomplish that each function must receive the sys.argv[1:] list from the caller.
import src

def test_parse_arg(argv):
    arg = src.parse_arg(argv)
    print(arg)

def test_read_data(argv):
    data = src.read_data()

    if(len(data) > 0):
        for i in range(0, 2):
            print("{}\n".format(data[i][5]))
    else:
        print("\nread_data failure.\n\n")

def test_search_schooldesc(argv):

    data = src.read_data()

    results = src.search_method(src.SRCH_SCHOOLDESC, data, "SOUTH")

    if len(results) >= 10:
        # Print only 10 results for testing because they are always numerous
        for i in range(0, 10):
            print("PAIRID: {}, SCHOOLDESC: {}". format(results[i][src.POS_PARID], \
                                                    results[i][src.POS_SCHOOLDESC]))

def test_search_parid(argv):

    data = src.read_data()

    results = src.search_method(src.SRCH_PARID, data, "0568E00072000000")

    if len(results) > 0:
        print("PAIRID: {}, SCHOOLDESC: {}". format(results[0][src.POS_PARID], \
                                                    results[0][src.POS_SCHOOLDESC]))





    