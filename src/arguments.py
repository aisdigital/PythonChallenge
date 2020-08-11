import argparse


class Arguments():
    def __init__(self, argv):
        parser = argparse.ArgumentParser()

        parser.add_argument('-o',
                            '--output',
                            dest='output',
                            type=str,
                            help='Relative path to the directory to write the output file')

        arg_group = parser.add_mutually_exclusive_group(required=True)
        arg_group.add_argument('--filter-school-desc',
                               dest='school_desc',
                               type=str,
                               help='Seach all the entries that contains the SCHOOL_DESC')

        arg_group.add_argument('--find-pair-id',
                               dest='pair_id',
                               type=str,
                               help='Seach the entries that has the PAIR_ID')

        arg_group.add_argument('--sale-summary',
                               dest='sale_summary',
                               action='store_true',
                               help='Show summary of how many sales for each SALEDESC')

        args = parser.parse_args()

        self.filter_by_school_desc = args.school_desc is not None
        self.school_desc = args.school_desc

        self.find_pair_id = args.pair_id is not None
        self.pair_id = args.pair_id

        self.show_sale_summary = args.sale_summary

        self.write_output_to_file = args.output is not None
        self.output_path = args.output

