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
dump_path = "../../dumps/item.csv"
nbt_path = "./chapters/3b630358"

saplings = {
    'minecraft:sapling': range(0, 6),
    'abyssalcraft:dltsapling': range(0, 1),
    'abyssalcraft:dreadsapling': range(0, 1),
    'aether_legacy:skyroot_sapling': range(0, 1),
    'aether_legacy:golden_oak_sapling': range(0, 1),
    'biomesoplenty:sapling_0': range(0, 8),
    'biomesoplenty:sapling_1': range(0, 8),
    'biomesoplenty:sapling_2': range(0, 8),
    'extrautils2:ironwood_sapling':range(0, 2),
    'tconstruct:slime_sapling':range(0, 3)
}
counter = 0
for k, v in saplings.items():
    for meta in v:
        quest_tag = nbt.NBTTagCompound()
        quest_tag['tasks'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
        task = nbt.NBTTagCompound()
        task['type'] = nbt.NBTTagString('item')
        task['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
        task['count'] = nbt.NBTTagLong(64)
        name = k + " 1 " + str(meta)
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
        


file = open(dump_path)
strings = file.readlines()
file.close()


for s in strings:
   if re.match("harvestcraft:[^_]*_sapling", s):
        quest_tag = nbt.NBTTagCompound()
        quest_tag['tasks'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
        task = nbt.NBTTagCompound()
        task['type'] = nbt.NBTTagString('item')
        task['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
        task['count'] = nbt.NBTTagLong(64)
        name = s.split(',')[0]
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
        
        



    
