import os
import simplejson as json

from csv import DictReader
from datetime import datetime
from collections import Counter

class DataContainer():
    def __init__(self, path: str):
        self.csv_data = {}
        self._load(path)

    def _load(self, path):
        abs_path = os.path.abspath(path)

        try:
            with open(abs_path, mode='r') as csv_file:
                self.csv_data = {row['PARID']: row for row in DictReader(csv_file)}

        except FileNotFoundError as e:
            print(f"No Data Loaded: couldn't read File {abs_path}\n{e}")

    def search_by_school_desc(self, data):
        pair_key = 'PARID'
        school_desc_key = 'SCHOOLDESC'
        results = []

        try:
            for item in self.csv_data.values():
                if data in item[school_desc_key]:
                    results.append(
                        {pair_key: item[pair_key], school_desc_key: item[school_desc_key]})
        except KeyError as e:
            print(f"Data doesn't has required key!\n{e}")

        return results

    def search_by_pair_id(self, key):
        return json.dumps(self.csv_data[key]) if key in self.csv_data else '{}'

    def get_sale_summary(self):
        key = 'SALEDESC'
        return json.dumps(Counter([item[key] for item in self.csv_data.values()]))

    def write(self, data, path, date=datetime.now()):
        abs_path = os.path.abspath(path)
        file_path = os.path.join(
            abs_path, f'results-{date.isoformat()}.txt')
        try:
            with open(file_path, mode='w') as f:
                f.write(data)
        except FileNotFoundError as e:
            print(e)
