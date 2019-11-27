
import sys, os

file_path = os.join(".workspace", "temp_adv.txt")

s = ""
with open(file_path, encoding='utf-8') as file:
    s = file.read()

s = s.replace("fvspve.quest.advancement_", "")
s = s.split("\n")

for line in s:
    

with open(file_path, "w", encoding="utf-8") as file:
    file.write(s)
