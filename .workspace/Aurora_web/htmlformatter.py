
from lxml import etree
path = ".workspace/Aurora_web/pages/KubeJS Documentation - net.minecraftforge.event.RegistryEvent$MissingMappings$Mapping.html"
file = open(path)
s = file.read()
s = s.replace(">", ">\n")
with open(".workspace/Aurora_web/pages/formatted.html", "w") as f:
    f.write(s)
