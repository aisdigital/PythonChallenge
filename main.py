import sys

import src.api_back as api
import src.supply as sply


def main(argv):
    if argv[0] == '--sale-summary':
        api.sale_desc()
        return

    try:
        _field = argv[0]
        _value = argv[1]
    except:
        print('Not correct parameters')
        return

    n_parameters = 4  # To be sure of args precessing

    if len(sys.argv) > n_parameters:
        if str(argv[2]) == "--output":
            api.dealing_arguments(_field, _value, argv[3])
    else:
        api.dealing_arguments(_field, _value)

if __name__ == '__main__':
    main(sys.argv[1:])
