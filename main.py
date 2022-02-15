import sys
import tests as t
import src as s

def app(argv):
    data = s.read_data()

    if len(data) < 0:
        return

    arg_list = s.parse_arg(argv)

    if arg_list["srch_type_code"] == s.NO_ARG:
        if "out" in arg_list:
            if arg_list["out"] == s.M_TXT: 
                print("\nPlease, enter the path to save the results.\n")
        else:
            print("\nInvalid command.\n")
    elif arg_list["srch_type_code"] == s.SRCH_SCHOOLDESC:
        results = s.search_method(s.SRCH_SCHOOLDESC, data, arg_list["srch_key"])
        if (len(results) > 1):
            # Print only 10 results for testing because they are always numerous. Also skip the
            # columns names row.
            for i in range(1, len(results)):
                print("\nPAIRID: {}, SCHOOLDESC: {}\n". format(results[i][s.POS_PARID], \
                                                        results[i][s.POS_SCHOOLDESC]))
            if arg_list["out"] == s.Y_TXT:
                s.export_results(results, arg_list["srch_out_path"])
            elif arg_list["out"] == s.Y_SALES:
                # The --sale-summary option has not been implemented yet. It only makes sense
                # with search by SCHOOLDESC, which can yields more the one result, although
                # there are some duplicate PAIRID entries in the CSV file.
                print("\n'--sale-summary' option is not implemented yet.\n")
        else:
            print("\nNo results found.\n")
    elif arg_list["srch_type_code"] == s.SRCH_PARID:
        results = s.search_method(s.SRCH_PARID, data, arg_list["srch_key"])
        if (len(results) > 1):
            # Skip the columns names row
            # P.S.: The PAIRID is not unique
            print("\nPAIRID: {}, SCHOOLDESC: {}\n". format(results[1][s.POS_PARID], \
                                                        results[1][s.POS_SCHOOLDESC]))
            if arg_list["out"] == s.Y_TXT:
                s.export_results(results, arg_list["srch_out_path"])
            elif arg_list["out"] == s.Y_SALES:
                # The --sale-summary option has not been implemented yet. It only makes sense
                # with search by SCHOOLDESC, which can yields more the one result, although
                # there are some duplicate PAIRID entries in the CSV file.
                print("\n'--sale-summary' option is not implemented yet.\n")
        else:
            print("\nNo results found.\n")
    else:
        # This is actually an impossible situation
        print("\nInvalid command.\n")

def main(argv):

# To run an unity test, comment the call for app(argv) and uncomment the call for the desired
# test function.
# Then run: python -m main ...
# It is not necessary to follow the command line standard with the test functions since their goal
# is to test every aspect of the application, including the command interpretation.

    # t.test_parse_arg(argv) # To test parse_arg function
    # t.test_read_data(argv) # To test read_data function
    # t.test_search_schooldesc(argv) # To test search by SCHOOLDESC functionality
    # t.test_search_parid(argv) # To test search by PARID functionality
    # t.test_export_results(argv) # To test export results (to TXT) functionality

    # This function implements the application logic
    app(argv)

if __name__ == '__main__':
    main(sys.argv[1:])
