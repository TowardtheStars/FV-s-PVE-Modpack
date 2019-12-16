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
    return hex(n)[2:]

dump_path = "../../dumps/item.csv"
nbt_path = "./chapters/6c4b954f"

file = open(dump_path)
strings = file.readlines()
file.close()
counter = 0

for s in strings:
   if re.match("harvestcraft:[^_]*_sapling", s):
        quest_tag = nbt.NBTTagCompound()
        quest_tag['tasks'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
        task = nbt.NBTTagCompound()
        task['type'] = nbt.NBTTagString('item')
        task['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
        task['count'] = nbt.NBTTagLong(64)
        name = s.split('_')[0] + 'item'
        print(name)
        task['item'] = nbt.NBTTagString(name)
        task['consume'] = nbt.NBTTagByte(1)
        quest_tag['tasks'].append(task)
        quest_tag['x'] = nbt.NBTTagDouble(counter // 6)
        quest_tag['y'] = nbt.NBTTagDouble(counter % 6)
        quest_tag['rewards'] = nbt.NBTTagList(tag_type=nbt.TAG_Compound)
        reward = nbt.TAG_Compound()
        reward['ftb_money'] = nbt.NBTTagLong(5)
        reward['type'] = nbt.NBTTagString('ftbmoney:money')
        reward['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
        quest_tag['rewards'].append(reward)
        counter += 1
        nbt.write_to_nbt_file(os.path.join(nbt_path, gen_id()+".nbt"), quest_tag)
        

                  

        
