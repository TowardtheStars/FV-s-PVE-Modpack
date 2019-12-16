import python_nbt.nbt as nbt
from python_nbt import JavaInteger as JavaInt
import os
from numpy import random

root = "./config/ftbquests/normal/chapters"
result = ".workspace/nbt/chapters/1a11ff42"

id_list = []

def add_dir(path):
    for directory in os.listdir(path):
        if directory not in ['chapter.nbt', 'index.nbt']:
            if os.path.isdir(os.path.join(path, directory)):
                add_dir(os.path.join(path, directory))
            else:
                directory = os.path.splitext(directory)[0]
            id_list.append(directory)

add_dir(root)

def gen_id(n=0):
    while n in id_list or n == 0 or n == 1:
        n = random.randint(2, 0x80000000)

    id_list.append(hex(n)[2:])
    return hex(n)[2:]

def rewards(money):
    result = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
    r = nbt.NBTTagCompound()
    r['ftb_money'] = nbt.NBTTagLong(money)
    r['type'] = nbt.NBTTagString('ftbmoney:money')
    r['uid'] = nbt.NBTTagInt(JavaInt.to_signed(gen_id(), 16))
    result.append(r)
    return result


class Item:
    def __init__(self, idx, meta, tag):
        self.idx = idx
        self.meta = meta
        self.tag = tag

def tasks(item, count):
    result = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
    r = nbt.NBTTagCompound()
    r['item'] = nbt.NBTTagString(item.idx)
    r['type'] = nbt.NBTTagString('item')
    r['uid'] = nbt.NBTTagInt(JavaInt.to_signed(gen_id(), 16))
    result.append(r)
    return result

import xlrd

wb = xlrd.open_workbook(".workspace/nbt/shop.xlsx")

sell_sheet = wb.sheet_by_name('sell')

sell_sheet.get_rows()
