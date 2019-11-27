import json, xlrd, pysnooper, os, sys
import numpy as np

print("Exporting config file for bountiful...")

config_json_path = os.path.join(".", "config", "bountiful", "bounties.json")
config_file_path = os.path.join(".", "config", "bountiful", "bountiful.cfg")
workbook_path = os.path.join(".", ".workspace", "12th物价表.xlsx")

file = open(config_json_path, "w")
workbook = xlrd.open_workbook(workbook_path)
bounties = workbook.sheet_by_name("bounties")
data = bounties.get_rows()
data = [[cell.value for cell in entry] for entry in data if (not str(entry[0].value).startswith("#")) and (not entry[0].value == "")]


def get_json_dict_from_data(entry):
    result = {}
    result["content"] = str(entry[0])
    result["amount"] = {}
    result["amount"]["min"] = int(entry[1])
    result["amount"]["max"] = int(entry[2])
    result["unitWorth"] = int(entry[3])
    result["weight"] = int(entry[4])
    if entry[5] != "":
        result["nbt_data"] = str(entry[5])
    if entry[6] != "":
        result["stages"] = []
        result["stages"].extend([c for c in entry[6:] if c != ""])
    return result

data = [get_json_dict_from_data(row) for row in data]

json.dump(data, file, indent=2)

file.close()

print("Finished")
