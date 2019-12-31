import python_nbt.nbt as nbt
import os
from numpy import random
from python_nbt import JavaInteger

id_list = set()
root = os.path.join("ftbquests","normal","chapters")

def gen_id(n=0, base=10):
    if isinstance(n, str):
        n = int(n, base)
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
            if directory not in id_list:
                id_list.add(directory)
            else:
                print("Collision detected! id: %s, %d" % (directory, JavaInteger.to_signed(directory, base=16)))
    return

add_dir(root)


to_merge = os.path.join("ftbquests","to_merge","chapters")

add_dir(to_merge)

print("Collision test finished. Any collision should be printed above.")

"""
for directory in os.listdir(to_merge):
    if os.path.isdir(os.path.join(path, directory)):
        new_dir_id = gen_id(directory, base=16)
        os.mkdir(os.path.join(root, new_dir_id))
        with open(os.path.join(to_merge, directory, 'chapter.nbt'), 'rb') as chapter_file:
            with open(os.path.join(root, new_dir_id, 'chapter.nbt'),'wb') as new_file:
                new_file.write(chapter_file.read())
        for quest_file in os.listdir(os.path.join(to_merge, directory)):
            if quest_file != "chapter.nbt":
                quest_id = os.path.splitext(quest_file)[0]
                new_id = gen_id(quest_id)
"""
                


