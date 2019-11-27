
import os
path = "./build/mod_list.txt"
print("Updating mod list")
counter = 0
with open(path, "w", encoding="utf-8") as file:
    file.write("# encoding = UTF-8\n")
    for mod in os.listdir("mods"):
        if os.path.isfile("mods/" + mod):
            print("Mod file: \"%s\" detected." % mod)
            counter += 1
            file.write(os.path.splitext(mod)[0] + "\n")
print("Mod count: %d" % counter)
