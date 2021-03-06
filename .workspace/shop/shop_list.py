import xlrd
import os, sys
import csv, json
import pysnooper
import numpy as np

print("Reading shop list")
root = "./.workspace/shop/"
config_path = "config/adminshop/shop.csv"
workbook = xlrd.open_workbook(os.path.join(root, "shoplist.xlsx"))
header = workbook.sheet_by_name("shop head")
buy_list_sheet = workbook.sheet_by_name("shop buy")
sell_list_sheet = workbook.sheet_by_name("shop sell")

file = open(config_path, "w")

output = csv.writer(file, dialect=csv.unix_dialect)

def gen_rows(sheet):
    return [[int(c.value) if str(c.value)[-1] == "0" and str(c.value)[-2] == "." else str(c.value) for c in r if c.value != ""] for r in sheet.get_rows()]

print("Exporting config file for admin shop...")
output.writerows(gen_rows(header))
output.writerows([[],[]])
output.writerows(gen_rows(buy_list_sheet))
output.writerows([[],[]])
output.writerows(gen_rows(sell_list_sheet))
print("Finished")
file.close()

# print("Press any key to quit")
# sys.stdin.readline()
