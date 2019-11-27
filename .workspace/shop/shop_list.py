import xlrd
import os, sys
import csv, json
import pysnooper
import numpy as np

print("Reading shop list")
workbook = xlrd.open_workbook("./.workspace/shop/" + "shoplist.xlsx")
header = workbook.sheet_by_name("shop head")
buy_list_sheet = workbook.sheet_by_name("shop buy")
sell_list_sheet = workbook.sheet_by_name("shop sell")

file = open("./config/adminshop/shop.csv", "w")

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

print("Exporting shop list pdf..")

print("Parsing shop list")
category_buy_name = []
category_sell_name = []

buy_list = {}
sell_list = {}

BUY = True
SELL = False

class Entry:

    names_loaded = False
    names_dict = {}
    icons_path = "./.workspace/icons"

    @staticmethod
    def load_names():
        for directory in os.listdir(Entry.icons_path):
            file = open(os.path.join(Entry.icons_path, directory, "_names.json"), "r", encoding="utf-8")
            Entry.names_dict.update(json.load(file))
        Entry.names_loaded = True

    def __init__(self, item:str, price:float, category:int, shop_mode:bool):
        spl = item.split(":", 1)
        self._mod_id = spl[0]
        spl = spl[1].split(" ", 1)
        if len(spl) < 2:
            spl.append("")
        self._item, self._nbt = tuple(spl)
        self._item = self._item.split(":", 1)
        self._metadata = 0
        if len(self._item) == 2:
            self._metadata = int(self._item[1])
        self._item = self._item[0]
        self._price = price
        if shop_mode == BUY:
            buy_list.get(category_buy_name[category]).append(self)
        elif shop_mode == SELL:
            sell_list.get(category_sell_name[category]).append(self)

    @property
    def mod_id(self):
        return self._mod_id or ""

    @property
    def item_id(self):
        return self._item or ""

    @property
    def metadata(self) -> int: 
        return self._metadata or 0

    @property
    def unlocalized_name(self):
        return self.mod_id + ":" + self.item_id + ":%d" % self.metadata
    
    @property
    def pic_path(self):
        raw =  ".workspace/icons/{modid}/{modid}__{name}__{metadata}.png".format(modid=self.mod_id, name=self.item_id, metadata=self.metadata)
        return raw

    @property
    def localized_name(self):
        if not Entry.names_loaded:
            Entry.load_names()
        return Entry.names_dict.get(self.unlocalized_name, "")

    @property
    def price(self):
        return self._price or 0.0

    def __repr__(self):
        raw = "\t\\includegraphics{" + self.pic_path + "} & " 
        raw2 = self.localized_name + " &%.2f" % self.price + "\\\\\n\t\\hline\n"
        raw2 = raw2.replace("_", "\\_", -1)
        return raw + raw2
        # return raw.replace("_", "\\_", -1)

    def __str__(self):
            return self.__repr__()

for row in header.get_rows():
    if row[0].value == "Buy Category Names:":
        category_buy_name = [str(c.value) for c in row[1:] if str(c.value) != ""]
    if row[0].value == "Sell Category Names:":
        category_sell_name = [str(c.value) for c in row[1:] if str(c.value) != ""]

for names in category_buy_name:
    buy_list[names] = list()

for names in category_sell_name:
    sell_list[names] = list()

for row in buy_list_sheet.get_rows():
    if row[0].value == "buy":
        Entry(row[1].value, float(row[2].value), int(row[3].value), BUY)

for row in sell_list_sheet.get_rows():
    if row[0].value == "sell":
        Entry(row[1].value, float(row[2].value), int(row[3].value), SELL)

print("Parse complete.")

def generate_latex():
    print("Generating LaTeX")
    header_str = \
    """
    \\documentclass[UTF8]{ctexart}
    \\usepackage{graphicx}
    \\usepackage{longtable}
    \\usepackage{multirow}
    \\usepackage{booktabs}
    \\usepackage{makecell}
    \\title{12周目价目表}
    \\begin{document}{}
    \\maketitle

    """
    latex_file_path = ".workspace/shop.tex"

    latex_file = open(latex_file_path, "w", encoding="utf-8")
    latex_file.writelines(header_str)


    def make_chart(goods_list):
        for k, v in goods_list.items():
            latex_file.writelines(
    """
    \\subsection{%s}
    \\begin{longtable}[]{|p{1cm}|p{8cm}|p{1.5cm}|}
    \\toprule
    图标 & 中文名 & 价格\\\\
    \\midrule
    """
                % k
            )
            latex_file.writelines(map(str, v))
            latex_file.writelines(
    """
    \\end{longtable}
    """
            )

    latex_file.writelines("\\section{玩家可买入}\n")
    make_chart(buy_list)
    latex_file.writelines("\\section{玩家可卖出}\n")
    make_chart(sell_list)

    latex_file.writelines("\\end{document}\n")
    latex_file.close()

    print("LaTeX generated.")
