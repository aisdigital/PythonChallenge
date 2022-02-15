import sys
import tests as t

def main(argv):
# To run an unity test, comment the call for app(argv) and uncomment the call for the desired
# test function.

    # t.test_parse_arg(argv) # Testing parse_arg function
    # t.test_read_data(argv) # Testing read_data function
    # t.test_search_schooldesc(argv) # Testing search by SCHOOLDESC functionality
    # t.test_search_parid(argv) # Testing search by PARID functionality
    t.test_export_results(argv) # Testing export results (to TXT) functionality

if __name__ == '__main__':
    main(sys.argv[1:])
