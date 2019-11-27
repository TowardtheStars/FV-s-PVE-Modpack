
import json, csv, pysnooper, os

# json_path = "saves/1_99_6/betterquesting/QuestDatabase.json"
json_path = os.path.join(".workspace/quest_names/QuestDatabase_backup.json")

csv_path = ".workspace/quest_names/quest_names.csv"

lang_path = ".workspace/quest_names/modpack_strings/assets/fvspve/lang/template.lang"

finished_prefix = "fvspve"
seperator = "."

quest_database_key = "questDatabase:9"
quests_key_format = "%d:10"
quest_prop_loc = ("properties:10", "betterquesting:10")
quest_name_key = "name:8"
quest_desc_key = "desc:8"
quest_type_key = "taskID:8"
quest_task_key = "tasks:9"

json_dict = json.load(open(json_path))

def get_database():
    return json_dict.get(quest_database_key)

def get_quest_property(idx:int):
    return get_quest(idx).get(quest_prop_loc[0]).get(quest_prop_loc[1])

def get_quest_name(idx:int) -> str:
    return get_quest_property(idx).get(quest_name_key)

def get_quest_desc(idx:int):
    return get_quest_property(idx).get(quest_desc_key)

def get_quest(idx:int):
    return get_database().get(quests_key_format % idx)

def get_quest_tasks(idx:int):
    return get_quest(idx).get(quest_task_key)

"""
Task type without prefix
"""
def get_quest_task_type(idx:int):
    try:
        return get_quest_tasks(idx).get("0:10").get(quest_type_key).split(":")[1]
    except AttributeError:
        return None
    
def set_quest_desc_key(idx:int, keyname:str=None):
    json_dict[quest_database_key][quests_key_format % idx][quest_prop_loc[0]][quest_prop_loc[1]][quest_desc_key] = "fvspve.quest." + keyname + ".desc"

def set_quest_name_key(idx:int, keyname:str=None):
    json_dict[quest_database_key][quests_key_format % idx][quest_prop_loc[0]][quest_prop_loc[1]][quest_name_key] = "fvspve.quest." + keyname + ".name"

"""
Exe after updating names in quest_names
"""
def gen_quest_name_and_lang_file():
    _file = open(csv_path, "r", encoding='gbk')
    csvfile = csv.reader(_file)
    lang_file = open(lang_path, "w", encoding="utf-8")
    for row in csvfile:
        quest_id = int(row[0])
        name = row[1]
        name = name.replace(" ", "")
        name_v = row[2]
        desc_v = ""
        set_quest_name_key(quest_id, name)
        set_quest_desc_key(quest_id, name)
        lang_file.write(get_quest_name(quest_id) + "=" + name_v + "\n")
        lang_file.write(get_quest_desc(quest_id) + "=" + desc_v + "\n")
    _file.close()
    lang_file.close()
    json_file = open(".workspace/quest_names/database.json", "w", encoding='utf-8')
    json.dump(json_dict, json_file,indent=2)
    json_file.close()

def get_type_keywords(q_type:str, task:dict)->str:
    result = ""

    if q_type == "retrieval":
        for item in task.get("requiredItems:9").values():
            result = item.get("id:8") + " x%d" % item.get("Count:3")
    elif q_type == "fluid":
        result = json.dumps(task.get("requiredFluids:9"))
    elif q_type == "scoreboard":
        result = task.get("scoreDisp:8") + ": " + task.get("scoreName:8") + " = " + str(task.get("target:3"))
    elif q_type == "hunt":
        result = task.get("target:8") + " x%d" % task.get("required:3")
    elif q_type == "advancement":
        result = task.get("advancement_id:8")
    return result

def gen_csv_file():
    # _file = open(csv_path, "w", encoding="gb2312")
    _file = open(csv_path, "w")
    csv_file = csv.writer(_file, dialect="unix")
    for quest in get_database().values():
        idx = quest.get("questID:3")
        name = get_quest_name(idx)

        if name.startswith(finished_prefix):
            name = name.split(seperator)[2]

        if get_quest_tasks(idx) == None:
            continue

        q_type = get_quest_task_type(idx)

        comment = ""
        comment += str(q_type)

        tasks = list(get_quest_tasks(idx).values())
        if len(tasks) != 0:
            comment = comment + "::" + get_type_keywords(q_type, tasks[0])
        # name = name.decode(encoding='utf-8').encode(encoding='gbk')
        csv_file.writerow([idx, name, name, comment])
    _file.close()

def get_quest_id(quest):
    return quest.get("questID:3")

def gen_adv_file():
    
    
    s_list = []
    for quest in get_database().values():
        idx = get_quest_id(quest)
        if get_quest_task_type(idx) == "advancement":
            name = get_quest_name(idx)
            desc = get_quest_desc(idx)
            task = list(get_quest_tasks(idx).values())[0]
            advID = task.get("advancement_id:8")
            s = "|" + advID + "|" + name + "|" + desc + "\n"
            s_list.append(s)
    s_list.sort()
    s_list = [s_list[i] for i in range(0, len(s_list), 2)]

    with open(".workspace/advancement.md", "w", encoding='utf-8') as file:
        file.write("# Advancements\n\n|ID|Name|Description\n|--|--|--\n")
        file.writelines(s_list)
gen_adv_file()