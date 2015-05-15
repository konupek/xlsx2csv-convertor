# -*- coding: utf-8 -*-
import xlrd
import csv
import glob
import unicodedata
import string
from os import sys

class Convertor:
    sheet_names = []

    def remove_accents(self, data):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in valid_chars).lower()

    def verify_uniquenes(self, sheetname, idx):
        print(sheetname);
        if sheetname in self.sheet_names:
            sheetname = sheetname + "_" + str(idx+1)
            return self.verify_uniquenes(sheetname, idx)
        else:
            self.sheet_names.append(sheetname)
            return sheetname

    def format_filename(self, s, idx):
        s = s.replace(' ','_')
        s = self.remove_accents(s)
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        if not filename:
            filename = "sheet" + str(idx+1);
        return self.verify_uniquenes(filename, idx)

    def convert(self, src, dest, name_prefix):
        files_extension = glob.glob(src + '*.*')
        files_all = glob.glob(src + '*')
        files = list(set(files_all) - set(files_extension))
        for xls_file in files:
            self.sheet_names = []
            self.csv_from_excel(xls_file, dest + name_prefix + '.')

    def csv_from_excel(self, excel_file, destination):
        workbook = xlrd.open_workbook(excel_file)
        all_worksheets = workbook.sheet_names()
        for idx, worksheet_name in enumerate(all_worksheets):
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(destination + ''.join([self.format_filename(worksheet_name, idx),'.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
            your_csv_file.close()