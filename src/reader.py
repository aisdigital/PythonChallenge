import csv
import json

INPUT_FILE = './input/property_sales_transactions.csv'


def get_summary():
    with open(INPUT_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        sale_descs = list(map(lambda row: row['SALEDESC'], reader))

        result = {key: sale_descs.count(key) for key in set(sale_descs)}

        return json.dumps(result, indent=2)


def find_pair_id(pair_id):
    with open(INPUT_FILE, mode='r') as file:
        reader = csv.DictReader(file)

        # The result is a list because there are duplicated PARID
        result = [row for row in reader if row['PARID'] == pair_id]

        return json.dumps(result, indent=2)


def filter_by_school_desc(school_desc):
    with open(INPUT_FILE, mode='r') as file:
        reader = csv.DictReader(file)

        # The result is a list because there are duplicated PARID
        result = [row for row in reader if school_desc in row['SCHOOLDESC']]

        return json.dumps(result, indent=2)
