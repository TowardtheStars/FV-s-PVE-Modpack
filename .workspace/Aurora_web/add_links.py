import re, os, pysnooper

path = ".workspace/Aurora_web/test_result.md"
dst_path = ".workspace/Aurora_web/add_link.md"

src = open(path)
lines = src.readlines()
src.close()

toc_list = [line for line in lines if line.startswith('#')]
link_list = [entry.split("# ")[1][:-1] for entry in toc_list]
link_pattern = ""

for toc in link_list:
    link_pattern += "|" + toc
link_pattern = link_pattern[1:]

link_pattern = link_pattern.replace("$", "\\$")
# print (link_pattern)
link_pattern ="[^a-zA-Z0-9$](" + link_pattern + ")[^a-zA-Z0-9$]"

# @pysnooper.snoop()
def convert_to_link(matched)->str:
    s = matched.string[matched.start():matched.end()]
    additional_end = s[-1]
    additional_start = s[0]
    s = s[1:-1]
    link = s.lower().replace(" ", "-").replace(".", "").replace("_","")
    return "%s[%s](#%s)%s" % (additional_start, s, link, additional_end)

lines = [re.sub(link_pattern, convert_to_link, line) if line not in toc_list else line for line in lines]
dst = open(dst_path, "w")
dst.writelines(lines)
dst.close()
