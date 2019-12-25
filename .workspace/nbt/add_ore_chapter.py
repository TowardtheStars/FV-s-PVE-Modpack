import python_nbt.nbt as nbt
import os, csv, re
from numpy import random
from python_nbt import JavaInteger

id_list = set()
root = "../../config/ftbquests/normal/chapters"

def gen_id(n=0):
    n = n & 0xffffffff
    value = hex(n)
    value = value[2:]
    value = "0" * (8 - len(value)) + value
    while value in id_list or n == 0 or n == 1:
        n = random.randint(-0x80000000, 0x80000000)
        n = n & 0xffffffff
        value = hex(n)
        value = value[2:]
        value = "0" * (8 - len(value)) + value
    id_list.add(value)
    return value

def add_dir(path):
    for directory in os.listdir(path):
        if directory not in {'chapter.nbt', 'index.nbt'}:
            if os.path.isdir(os.path.join(path, directory)):
                add_dir(os.path.join(path, directory))
            else:
                file = nbt.read_from_nbt_file(os.path.join(path,directory))
                if 'tasks' in file.keys():
                    for task in file.get('tasks'):
                        id_list.add(gen_id(task['uid'].value))
                if 'rewards' in file.keys():
                    for reward in file.get('rewards'):
                        id_list.add(gen_id(reward['uid'].value))
                directory = os.path.splitext(directory)[0]
            id_list.add(directory)

add_dir(root)

dump_path = "crafttweaker.log"

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
            

            
