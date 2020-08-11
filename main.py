"""
AIS Python Challenge - Data search
 @author Rafael Lima
"""

import sys
import csv
import json
import argparse

#PARID,PROPERTYHOUSENUM,PROPERTYFRACTION,PROPERTYADDRESSDIR,PROPERTYADDRESSSTREET,PROPERTYADDRESSSUF,PROPERTYADDRESSUNITDESC,PROPERTYUNITNO,PROPERTYCITY,PROPERTYSTATE,PROPERTYZIP,SCHOOLCODE,SCHOOLDESC,MUNICODE,MUNIDESC,RECORDDATE,SALEDATE,PRICE,DEEDBOOK,DEEDPAGE,SALECODE,SALEDESC,INSTRTYP,INSTRTYPDESC


def getdata(filename):
    """
    Get Data from CSV file
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        count = 0
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
    Get Data from CSV file
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        count = 0
        for row in datareader:
            if row["PARID"] == pairid:
                yield row


def getsalesummary(filename):
    """
    Get Data from CSV file
    """
    saleSummary = {}
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        count = 0
        for row in datareader:
            if row["SALEDESC"] in saleSummary:
                saleSummary[row["SALEDESC"]] += 1
            else:
                saleSummary[row["SALEDESC"]] = 1

    return saleSummary


def writeReport(filedir,text):
    # Generate filename
    filename = filedir+"/"+"results-"+"timestamp"+".txt"

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
    parser.add_argument("-o","--output",action='store_true',
                        help="Define Output directory")
    parser.add_argument("-c","--sales-summary",dest='salessumary',action='store_true',
                        help="Count how many per SALEDESC")

    # Evaluate Input arguments
    args = parser.parse_args()

    # Select Option and Perfom Required Filter
    if args.pairid:
        for i in getentry("input/property_sales_transactions.csv", args.pairid):
            print(i)
    elif args.schooldesc:
        for i in getschool("input/property_sales_transactions.csv", args.schooldesc):
            print(i)
    elif args.salessumary:
        for i in getsalesummary("input/property_sales_transactions.csv"):
            print(i)

    #if isFileReport:
    #    print(reportText)
    #else
    #    writeReport(filedir,reportText)

if __name__ == '__main__':
        main(sys.argv[1:])
