#!/usr/bin/env python3

import re
import sys
import csv
import tabula
import PyPDF2
import pandas as pd



def generate_csv(file):
    lastPage = PyPDF2.PdfReader(file).getNumPages()
    tabula.convert_into(file, "../data/test.csv", output_format="csv", pages = '1-{}'.format(lastPage))


def my_bank_statement():
    with open("../data/nyquistBankStatement.csv", "w") as wFile:
        wCsv = csv.writer(wFile)
        wCsv.writerow(['Posted Date', 'Value Date', 'Description', 'Debit', 'Credit', 'Balance'])
        with open('../data/test.csv') as rFile:
            csvFile = csv.reader(rFile)
            for line in csvFile:
                # print(line)
                pattern = r"NWAUKWA I.C|NWAUKWA STEPHEN|NWAUKWA ISAAC|ISAAC NWAUKWA"
                # pattern = r"CHINEDU|chinedu"
                result = re.search(pattern, line[2])
                # print(result)
                if result:
                    wCsv.writerow(line)

def generate_excel():
    read_file = pd.read_csv ('../data/nyquistBankStatement.csv')
    read_file.to_excel ('../data/nyquistBankStatement.xlsx', index = None, header=True)


if __name__ == "__main__":
    file = sys.argv[1]
    generate_csv(file)
    my_bank_statement()
    generate_excel()
