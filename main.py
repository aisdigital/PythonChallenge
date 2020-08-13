"""
AIS Python Challenge - Data search
 @author Rafael Lima
"""

import sys
import csv
import json
import argparse
import datetime

#PARID,PROPERTYHOUSENUM,PROPERTYFRACTION,PROPERTYADDRESSDIR,PROPERTYADDRESSSTREET,PROPERTYADDRESSSUF,PROPERTYADDRESSUNITDESC,PROPERTYUNITNO,PROPERTYCITY,PROPERTYSTATE,PROPERTYZIP,SCHOOLCODE,SCHOOLDESC,MUNICODE,MUNIDESC,RECORDDATE,SALEDATE,PRICE,DEEDBOOK,DEEDPAGE,SALECODE,SALEDESC,INSTRTYP,INSTRTYPDESC


def getdata(filename):
    """
    Get Data from CSV file
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            yield row


def getschool(filename,schooldesc):
    """
    Get Data from CSV file
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            if schooldesc in row["SCHOOLDESC"]:
                yield {"PARID":row["PARID"],"SCHOOLDESC":row["SCHOOLDESC"]}


def getentry(filename,pairid):
    """
    Get Entry by PAIRID
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            if row["PARID"] == pairid:
                yield row


def getsalesummary(filename):
    """
    Generate Sales Report
    """
    saleSummary = {}
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            if row["SALEDESC"] in saleSummary:
                saleSummary[row["SALEDESC"]] += 1
            else:
                saleSummary[row["SALEDESC"]] = 1

    return saleSummary


def writeReport(filedir,text):
    """
    Write file report
    """
    # Generate filename
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat().replace(":","")
    filename = filedir+"/"+"results-"+timestamp+".txt"

    # Write File
    reportFile = open(filename,"w")
    reportFile.write(text + '\n')
    reportFile.close()


def main(argv):
    """
    Main Function - Read Argments and Display help msg
    """

    # Create input arguments using argparse
    parser = argparse.ArgumentParser(prog="AIS Python Challenge")
    parser.add_argument("-s","--find-pair-school-desc",dest='schooldesc',action='store',
                        help="Search entries BY SCHOOLDESC")
    parser.add_argument("-i","--find-pair-id",dest='pairid',action='store',
                        help="Seach entry by PAIRID")
    parser.add_argument("-o","--output",action='store',
                        help="Define Output directory")
    parser.add_argument("-c","--sales-summary",dest='salessumary',action='store_true',
                        help="Count how many per SALEDESC")

    # Evaluate Input arguments
    args = parser.parse_args()

    # Select Option and Perfom Required Filter
    inputFileName = "input/property_sales_transactions.csv"
    reportText = ""
    if args.pairid:
        reportText = getentry(inputFileName, args.pairid)
    elif args.schooldesc:
        reportText = getschool(inputFileName, args.schooldesc)
    elif args.salessumary:
        reportText = getsalesummary(inputFileName)

    # Select Output and Generate Report
    if args.output:
        writeReport(args.output,str(reportText))
    else:
        print(reportText)


if __name__ == '__main__':
    main(sys.argv[1:])
