import sys
from src.storage import read_and_store_CSV
from src.query import search_by_school_desc, search_by_pair_id, sale_summary
from src.output import dump_result_txt


def main(argv):
    # obtain full arguments (starting with --) from argv array
    full_arguments = [key for key in argv if '--' in key]
    # obtain short arguments (starting with --) from argv array
    short_arguments = [key for key in argv if '-' in key]
    # read and store CSV file in memory
    data = read_and_store_CSV('./input/property_sales_transactions.csv')
    # array where the query results will be stored
    results = []
    # flag that checks if there's -o or --output amongst the arguments
    dump_in_file = ('--output' in full_arguments) or ('-o' in short_arguments)
    # if there's --filter-school-desc argument, call search_by_school_desc
    if '--filter-school-desc' in full_arguments:
        try:
            school_desc = argv[argv.index('--filter-school-desc') + 1]
            results.append("\nRESULT --filter-school-desc " + school_desc + ":")
            results.append(search_by_school_desc(data, school_desc, dump_in_file))
        except IndexError:
            print('ERROR: Missing argument in --filter-school-desc')
            sys.exit(1)
    # if there's --find-pair-id argument, call search_by_pair_id
    if '--find-pair-id' in full_arguments:
        try:
            pair_id = argv[argv.index('--find-pair-id') + 1]
            results.append("\nRESULT --find-pair-id " + pair_id + ":")
            results.append(search_by_pair_id(data, pair_id, dump_in_file))
        except IndexError:
            print('ERROR: Missing argument in --find-pair-id')
            sys.exit(2)
    # if there's --sale-summary argument, call sale_summary
    if '--sale-summary' in full_arguments:
        results.append('\nRESULT --sale-summary:')
        results.append(sale_summary(data, dump_in_file))
    # if there's --output argument, call dump_result_txt
    if '--output' in full_arguments:
        try:
            dump_result_txt(results, argv[argv.index('--output') + 1])
        except IndexError:
            print('ERROR: Missing argument in --output')
            sys.exit(3)
    # if there's -o argument, call dump_result_txt
    if '-o' in short_arguments:
        try:
            dump_result_txt(results, argv[argv.index('-o') + 1])
        except IndexError:
            print('ERROR: Missing argument in -o')
            sys.exit(3)


if __name__ == '__main__':
    main(sys.argv[1:])
