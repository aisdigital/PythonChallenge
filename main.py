import sys
import src.reader as reader
import src.writer as writer
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
        writer.wirte_to_file(args.output_path, result)
    else:
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
