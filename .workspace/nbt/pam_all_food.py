import python_nbt.nbt as nbt
import os, csv, re, json
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

print(len(id_list))

log_path = 'crafttweaker.log'

log_file = open(log_path)

ore_pattern = 'Ore entries for <ore:[a-zA-Z_][a-zA-Z0-9_]*> :'
def get_oredict(s):
    return s.split('<')[1].split('>')[0].split(':')[1]

item_pattern = '-<[^>]*>'
def get_item(s):
    s = s[2:-2]
    result = {}
    s = s.split(':')
    result['namespace'] = s[0]
    result['item'] = s[1]
    if len(s) == 3:
        result['meta'] = int(s[2]) if s[2] != '*' else -1
    return result

ore_dict = {}

ore = ''
for line in log_file.readlines():
    if re.match(ore_pattern, line):
        ore = get_oredict(line)
        ore_dict[ore] = []
    elif re.match(item_pattern, line):
        ore_dict[ore].append(get_item(line))

json_file = open('oredict.json', 'w', encoding='utf-8')
json.dump(ore_dict, json_file, indent=2)
json_file.close()

chapter = 'chapters/48b928ad'

counter = 0
def create_quest(item):
    global counter
    tag = nbt.NBTTagCompound()
    tag['x'] = nbt.NBTTagDouble(counter // 21 - 10)
    tag['y'] = nbt.NBTTagDouble(counter %  21 - 10)
    tag['rewards'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
    tag['tasks'] = nbt.NBTTagList(tag_type=nbt.NBTTagCompound)
    cmp_task = nbt.NBTTagCompound()
    cmp_task['consume'] = nbt.NBTTagByte(1)
    cmp_task['count'] = nbt.NBTTagLong(64)
    cmp_task['item'] = nbt.NBTTagString(item['namespace'] + ':' + item['item'])
    cmp_task['type'] = nbt.NBTTagString('item')
    cmp_task['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
    tag['tasks'].append(cmp_task)
    cmp_reward = nbt.NBTTagCompound()
    cmp_reward['ftb_money'] = nbt.NBTTagLong(50)
    cmp_reward['type'] = nbt.NBTTagString('ftbmoney:money')
    cmp_reward['uid'] = nbt.NBTTagInt(JavaInteger.to_signed(gen_id(), base=16))
    tag['rewards'].append(cmp_reward)
    nbt.write_to_nbt_file(os.path.join(chapter, gen_id() + '.nbt'), tag)
    print(item['namespace'],':',item['item'])
    counter += 1
    

for k, v in ore_dict.items():
    if k.startswith('food'):
        for item in v:
            if item['namespace'] == 'harvestcraft':
                create_quest(item)



