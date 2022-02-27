import csv
import json

class CsvOps():
    def __init__(self):
        self.filePath = './input/property_sales_transactions.csv'
    
    def searchSchoolDesc(self, entry):
        with open(self.filePath, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[12] == entry:
                    print("PAIRID", line[0])
                    print("\n")
                    print("SCHOOLDESC", line[12])
                    
    def searchByPairId(self, entry):
        with open(self.filePath, 'r') as file:
            reader = csv.reader(file)
            for count, line in enumerate(reader):
                if (count == 0):
                    csvFirstLine = line
                
                if line[0] == entry:
                    zippedLists = zip(csvFirstLine, line)
                    zip2dict = dict(zippedLists)
                    print(json.dumps(zip2dict))