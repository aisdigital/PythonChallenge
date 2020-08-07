import csv
import time
import json
import calendar

import src.supply as sply


def sale_desc():
    with open('./input/property_sales_transactions.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        aux_dict = {}

        for row in csv_reader:
            if row["SALEDESC"] in aux_dict:
                aux_dict[row["SALEDESC"]] += 1
            else:
                aux_dict[row["SALEDESC"]] = 0

        print(json.dumps(aux_dict, sort_keys=True, indent=4))


# Read .csv file
def list_interactor(_field, _value, _output=None):
    with open('./input/property_sales_transactions.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if _field == "SCHOOLDESC":
                if row[_field] == _value:
                    print("PARID -> ", row["PARID"], "\t SCHOOLDESC -> ", row["SCHOOLDESC"])

            elif _field == "PARID":
                if _output is None:  # FIXME
                    if row[_field] == _value:
                        print(json.dumps(row, sort_keys=True, indent=4))

                else:
                    if row[_field] == _value:
                        ts = calendar.timegm(time.gmtime())
                        filename = "results-" + str(ts) + ".txt"

                        myfile = open(filename, 'w')
                        myfile.write(json.dumps(row, sort_keys=True, indent=4))
                        myfile.close()


def dealing_arguments(_field, _value, _output=None):
    list_interactor(sply.first_argumet(_field), _value, _output)
