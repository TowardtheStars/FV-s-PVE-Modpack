import python_nbt.nbt as nbt
import os, csv, re, json
from numpy import random
from python_nbt import JavaInteger
from python_nbt._util import TypeRestrictedDict

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

target_root = "./chapters/ebeae9f8"

config_file = "../../config/apotheosis/enchantments.cfg"

def path_get(d, key_path):
    c = d
    for k in key_path:
        c = c[k]
    return c

def path_set(d, key_path, value):
    last_key = key_path[-1]
    c = d
    for k in key_path[:-1]:
        c = c[k]
    c[last_key] = value


import pysnooper
class Config(dict):
    def __init__(self, file=None):
        if file:
            self.from_file(file)
        else:
            pass
    # @pysnooper.snoop()
    def from_file(self, file):
        import re
        type_chr_dict = {
            'I':int,
            'D':float,
            'F':float,
            'B':int,
            'S':str,
        }
        
        if isinstance(file, str):
            file = open(file, encoding='utf-8')
        file = file.readlines()
        cur_field = []
        flag_is_list = False
        type_trans = None
        for line in file:
            if not re.match("(\s*#.*)|(\s*\n)", line): # Exclude comment line
                if not flag_is_list:
                    # see if field begin
                    field = re.match("[^\"]*\s\{", line) or re.match("\"[^\"]*\"", line)
                    if field:
                        field = field.group()[:-1]
                        while field[0] == " ":
                            field = field[1:]
                        while field[-1] == ' ':
                            field = field[:-1]
                        if field[0] == '\"':
                            field = field[1:]
                        cur_field.append(field)
                        path_set(self, cur_field, {})
                        continue
                    # See if field ends
                    elif re.match("[\s]*\}", line):
                        cur_field.pop()
                        continue
                    type_trans = type_chr_dict[re.search("[BDFIS]:", line).group()[0]]
                    name = re.search(":[^\"=]*=", line)
                    if not name:
                        name = re.search("\"[^\"=]*\"", line)
                    name = name.group()[1:-1]
                    flag_is_list = re.search("=[\s]*<[\s]*", line)
                    if not flag_is_list: # parsing value
                        v = type_trans(re.search("=.*\n", line).group()[1:-1])
                        cur_field.append(name)
                        path_set(self, cur_field, v)
                        cur_field.pop()
                    else:
                        # make a list, add name into path
                        cur_field.append(name)
                        path_set(self, cur_field, list())
                        cur_field.pop()
                        
                elif flag_is_list: # parsing config list when cur_field is not None
                    
                    # See if list ends
                    if re.match("[\s]*>[\s]*"):
                        cur_field.pop()
                    else: # should not end
                        v = type_trans(re.search("[^\s]*\n").group()[:-1])
                        path_get(self, cur_field).append(v)
        
                

f = Config(config_file)

ench_lvl = {}

for k, v in f.items():
    v = v.get('Max Level', None)
    if v:
        ench_lvl[k] = v


ench_id = {}
ench_name = {}
data_file = open("./enchants.txt", encoding="utf-8")

for line in data_file.readlines():
    k = re.search("<enchantment:[A-Za-z0-9_]+:[A-Za-z0-9_]+>", line)
    if k:
        k=k.group()[13:-1]
        _id = re.search("enchant id [0-9]+", line)
        if _id:
            _id = int(re.search("[0-9]+" , _id.group()).group())
            ench_id[k]=_id
        name = re.search("> - [^\s]* ", line)
        if name:
            name = name.group()[4:-1]
            ench_name[k] = name

def intoRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dic_1=['','I','II','III','IV','V','VI','VII','VIII','IX']
    dic_10 = ['', 'X','XX',  'XXX','XL','L','LX', 'LXX','LXXX','XC']
    dic_100 = ['','C', 'CC',  'CCC', 'CD', 'D','DC',  'DCC', 'DCCC', 'CM',]
    dic_1000 = ['','M','MM','MMM']
    res = ''
    res = dic_1000[num//1000]+dic_100[(num%1000)//100]+dic_10[(num%100)//10]+dic_1[num%10]
    return res

ench_count = 0
def gen_quest(_id, name, lvl):
    quest = nbt.NBTTagCompound()
    quest['x']=nbt.NBTTagDouble(5.5 + ench_count // 7)
    quest['y']=nbt.NBTTagDouble(-1 + ench_count % 7)

    quest['tasks'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)

    task = nbt.NBTTagCompound()
    task['uid'] = nbt.NBTTagString(gen_id())
    task['type'] = nbt.NBTTagString('item')
    task['title']= nbt.NBTTagString('附魔书 - %s' % (name + (intoRoman(lvl) if lvl > 1 else '')))
    task['ignore_nbt'] = nbt.NBTTagByte(2)
    task['ignore_damage'] = nbt.NBTTagByte(1)
    task['item'] = nbt.NBTTagCompound()
    task['item']['id'] = nbt.NBTTagString("minecraft:enchanted_book")
    task['item']['tag'] = nbt.NBTTagCompound()
    task['item']['tag']['StoredEnchantments'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)

    enchantment = nbt.NBTTagCompound()
    enchantment['id'] = nbt.NBTTagShort(_id)
    enchantment['lvl'] = nbt.NBTTagShort(lvl)

    task['item']['tag']['StoredEnchantments'].append(enchantment)

    quest['tasks'].append(task)

    quest['rewards'] = nbt.NBTTagList(tag_type = nbt.NBTTagCompound)
    reward = nbt.NBTTagCompound()
    reward['uid'] = nbt.NBTTagString(gen_id())
    reward['type'] = nbt.NBTTagString('ftbmoney:money')
    reward['ftb_money'] = nbt.NBTTagLong(1000)
    quest['rewards'].append(reward)
    ench_count += 1
    return quest


log_file = open('./ench_max_lvl.csv', 'w', encoding='gbk')
for k in ench_id.keys():
    log_file.write(ench_name[k] + ','+ str(ench_lvl[k]) + '\n')
log_file.close()





