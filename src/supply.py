# Take '-' off the string and put string in CAPITAL LETTER
# 'string-string' -> 'STRINGSTRING


def transform_string(received_string):
    return received_string.replace('-', '').upper()


# Prepare first argument to search in .csv
def first_argumet(_field):
    result1 = _field.find('--filter')
    result2 = _field.find('--find')

    if result1 != -1:
        return transform_string(_field.split('--filter-', 1)[1])

    elif result2 != -1:
        return transform_string(_field.split('--find-', 1)[1])
