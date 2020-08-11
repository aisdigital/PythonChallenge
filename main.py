import sys
import os
import datetime
import src.reader as reader
from src.arguments import Arguments


def main(argv):
    args = Arguments(argv)

    result = ''

    if args.find_pair_id:
        result = reader.find_pair_id(args.pair_id)

    elif args.filter_by_school_desc:
        result = reader.filter_by_school_desc(args.school_desc)

    elif args.show_sale_summary:
        result = reader.get_summary()

    if args.write_output_to_file:
        date = datetime.datetime.now().isoformat()
        path = f'./{args.output_path}'
        
        if not os.path.exists(path):
            os.makedirs(path)

        with open(f'{path}/results-{date}.txt', mode='w') as out:
            out.write(result)

    else:
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
