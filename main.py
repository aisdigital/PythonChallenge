import sys
import os
import json

from csv import reader

def jsonFormat(row):
    x = {
    'PARID' : row[0],
    'PROPERTYHOUSENUM' : row[1],
    'PROPERTYFRACTION' : row[2],
    'PROPERTYADDRESSDIR' : row[3],
    'PROPERTYADDRESSSTREET' : row[4],
    'PROPERTYADDRESSSUF' : row[5],
    'PROPERTYADDRESSUNITDESC' : row[6],
    'PROPERTYUNITNO' : row[7],
    'PROPERTYCITY' : row[8],
    'PROPERTYSTATE' : row[9],
    'PROPERTYZIP' : row[10],
    'SCHOOLCODE' : row[11],
    'SCHOOLDESC' : row[12],
    'MUNICODE' : row[13],
    'MUNIDESC' : row[14],
    'RECORDDATE' : row[15],
    'SALEDATE' : row[16],
    'PRICE' : row[17],
    'DEEDBOOK' : row[18],
    'DEEDPAGE' : row[19],
    'SALECODE' : row[20],
    'SALEDESC' : row[21],
    'INSTRTYP' : row[22],
    'INSTRTYPDESC' : row[23],
    }
    return x

def SaveToFile(text, path):
    r = open(path, 'w')
    for row in text:
        r.write(row)
    r.close()

def main(argv):
    data =[]                
    print('Python Challenge')    
    print(os.path.dirname(__file__))    
    with open(os.path.dirname(__file__) + '\input\property_sales_transactions.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            data.append(row)
    path = ''
    if '-o' in argv:
        path = argv[argv.index('-o')+1]
    if '--output' in argv:
        path = argv[argv.index('--output')+1]
    print(path)
    result = []
    if '--filter-school-desc' in argv:
        for row in data:
            if argv[1] in row[12]:
                result.append(row[0] + ' ' + row[12])
        if len(path) > 0:
            SaveToFile(result, path)
        else:
            print(result)
    if '--find-pair-id' in argv:
        for row in data:
            if argv[1] in row[0]:
                result.append(json.dumps(jsonFormat(row), indent=5))
        if len(path) > 0:
            SaveToFile(result, path)
        else:
            print(json.dumps(jsonFormat(row), indent=5))
    
                

    
if __name__ == '__main__':
    main(sys.argv[1:])


    


