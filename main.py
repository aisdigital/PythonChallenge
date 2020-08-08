import os
import sys
import argparse

from src.data_container import DataContainer


def main(argv):
    parser = argparse.ArgumentParser(description='AIS - Python Challenge')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--filter-school-desc', dest='schooldesc', type=str,
                       help='''Search by all the entries that contains and show the PARID and SCHOOLDESC of each one''')
    group.add_argument('--find-pair-id', dest='pair_id', type=str,
                       help='''Find an entry by PARID and output the full entry in JSON format on the screen''')
    group.add_argument('--sale-summary', dest='sale_summary', action='count', default=0,
                       help='''show on the console a JSON summary of how many sales for each SALEDESC''')

    parser.add_argument('-o', '--output', dest='output_path', type=str,
                        help='''path to a directory where results will be dumped in ''')

    args = parser.parse_args()

    if args.schooldesc is None and args.pair_id is None and args.sale_summary == 0:
        parser.print_help()
        return

    results = None
    data_container = DataContainer(os.path.join(
        'input', 'property_sales_transactions.csv'))

    if args.schooldesc:
        results = data_container.search_by_school_desc(args.schooldesc)
    elif args.pair_id:
        results = data_container.search_by_pair_id(args.pair_id)
    elif args.sale_summary:
        results = data_container.get_sale_summary()

    if args.output_path:
        data_container.write(results, args.output_path)
    else:
        print(results)


if __name__ == '__main__':
    main(sys.argv[1:])
