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


def getscholl(filename,schooldesc):
    """
    Get Data from CSV file
    """
    with open(filename) as csvfile:
        datareader = csv.DictReader(csvfile)
        count = 0
        for row in datareader:
            if schooldesc in row["SCHOOLDESC"]:
                yield {row["PARID"],row["SCHOOLDESC"]}


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

    yield saleSummary


def writeReport(filedir,text):
    # Generate filename
    filename = filedir+"/"+"results-"+"timestamp"+".txt"

def main(argv):
    """
    Main Function - Read Argments and Display help msg
    """

    help_msg = """
    Use: python -m main.py [OPTION] [ARGUMENT]
    OPTIONS:
    \t-s,--find-pair-school-desk\t\tSearch entry by scholl id
    \t-i,--find-pair-id\t\tSearch entry by scholl id
    \t-o,--output\t\tSearch entry by scholl id
    \t-c,--sale-summary\t\tCount how many sales per SALEDESK
    """

    #isFileReport = False

    #print(help_msg)
    #getdata("input/property_sales_transactions.csv")

    #for i in getentry("input/property_sales_transactions.csv","9929X85746000000"):
    #    print(i)

    for i in getsalesummary("input/property_sales_transactions.csv"):
        print(i)

    #if isFileReport:
    #    print(reportText)
    #else
    #    writeReport(filedir,reportText)

if __name__ == '__main__':
    main(sys.argv[1:])
