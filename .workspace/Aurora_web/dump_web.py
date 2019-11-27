from urllib.request import urlopen
from lxml import etree
import re

root_url = "http://localhost:48574"

result = []
to_visit = ["/kubejs"]
target_path = ".workspace/Aurora_web/result.md"


while len(to_visit) != 0:
    if not to_visit[0] in result and to_visit[0].startswith("/kubejs"):
        html = etree.HTML(urlopen(root_url + to_visit[0]).read(), etree.HTMLParser())
        links = html.xpath("/html/body//a/@href")
        links = [l for l in links if not (l in to_visit) and not (l in result)]
        links = [l for l in links if l.startswith("/")]
        links = [l for l in links if re.search("java|javafx|sun|google|netty|lwjgl", l) is None]
        to_visit.extend(links)
        result.append(to_visit[0])
        # print(result)
    to_visit.pop(0)

def dump0(w):
    s = ""
    html = etree.HTML(urlopen(root_url + w).read(), etree.HTMLParser())
    tables = html.xpath ('/html/body/table')
    headers = html.xpath('/html/body/h2/text()')
    for table in tables:
        s += "## "
        s += headers[tables.index(table)]
        s += '\n\n'
        rows = table.xpath('tr')
        for head_col in rows[0].xpath('th/text()'):
            s += "|" + head_col
        s += "\n"
        for i in range(len(rows[0].xpath('th/text()'))):
            s += "|--"
        s += "\n"
        for row in rows[1:]:
            for col in row.xpath('td/text()|td/span/a/text()|td/span/text()'):
                s += "|" + col
            s += '\n'
        s += '\n---\n\n'
    s = s.replace("<", "\\<")
    return s

# s = dump0(webs[0])

def dump1(w):
    s = ""
    html = etree.HTML(urlopen(root_url + w).read(), etree.HTMLParser())
    tables = html.xpath ('/html/body/table')
    header = html.xpath ('/html/body/h2/text()')
    if len(header) > 0:
        s += "## " + header[0] + "\n\n"
    for table in tables:
        rows = table.xpath('tr')
        for head_col in rows[0].xpath('th/text()|th/*/text()'):
            s += "|" + head_col
        s += "\n"
        for i in range(len(rows[0].xpath('th'))):
            s += "|--"
        s += "\n"
        for row in rows[1:]:
            for col in row.xpath('td'):
                s += "|"
                for t in col.xpath('.//text()'):
                    s += t
            s += '\n'
        s += '\n---\n\n'
    s = s.replace("<", "\\<")
    return s


with open(target_path, "w") as file:
    file.write("# KubeJS Document\n\n")
    file.write(dump0(result[0]))
    for w in result[1:]:
        file.write(dump1(w))