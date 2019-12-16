import python_nbt.nbt as nbt
import os, csv, re
from numpy import random
from python_nbt import JavaInteger

id_list = []
root = "../../config/ftbquests/normal/chapters"

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
    value = hex(n)
    value = value[2:]
    value = "0" * (8 - len(value)) + value
    id_list.append(value)
    return value
dump_path = "./crafttweaker.log"
nbt_path = "./chapters/fb3b8b92"


ores = []
flag = False
with open(dump_path) as file:
    lines = file.readlines()
    for line in lines:
        if re.match('Ore entries for <ore:ore[^>]*> :', line):
            flag = True
        if flag and re.match('-<[^>]*>', line):
            ores.append(line[2:-2])
            flag = False

print(ores)
            

            
