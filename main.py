#!/usr/bin/env python3

import argparse
from src.csvOps import CsvOps

parser = argparse.ArgumentParser(description='Read CSV')

parser.add_argument('--filter-school-desc', type=str)
parser.add_argument('--find-pair-id', type=str)


args = parser.parse_args()

if __name__ == '__main__':
    csv0 = CsvOps()
    if args.find_pair_id is not None:
        csv0.searchByPairId(args.find_pair_id)
    elif args.filter_school_desc is not None:
        csv0.searchSchoolDesc(args.filter_school_desc)
        
    