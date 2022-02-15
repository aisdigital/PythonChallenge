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


    