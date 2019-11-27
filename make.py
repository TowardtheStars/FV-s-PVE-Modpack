# Fake makefile

import sys

__version = "2.0.1-alpha"

def parse_all() -> dict:
    result = {"prog":sys.argv[0]}
    counter = 0
    if len(sys.argv) != 1:
        for argv in sys.argv[1:]:
            if argv[0] == "-":
                if argv[1] == "-":
                    argv = argv.split("=", 1)
                    result[argv[0][2:]] = argv[1]
                else:
                    for c in argv[1:]:
                        result[c] = True
            else:
                result[counter] = argv
                counter += 1
    result["size"] = counter
    return result


import zipfile, os
from os.path import join

out_put_folder = "./build"


def _refresh_readme():
    readme = open("readme.md", "r", encoding="utf-8")
    readme_text = readme.read()
    readme.close()
    if not os.path.exists(out_put_folder):
        os.mkdir(out_put_folder)
    readme = open(join(out_put_folder, "readme.md"), "w", encoding="utf-8")
    readme_text = readme_text.replace("%{version}", __version)
    readme.write(readme_text)
    readme.close()


def _packup(silent_mode:bool=False):
    _refresh_readme()
    package = zipfile.ZipFile(join(out_put_folder, "FV's PVE v%s.zip" % (__version)), "w")
    files = [
        "config", 
        "mods", 
        "scripts",
        "kubejs",
        "mod_list.txt",
        "Modpack模式选择器.sh",
        "Modpack模式选择器.bat"
    ]
    dir_file_blacklist = [
        "jei",
        "jeresources",
        "simplelogin.cfg",
        "JustEnoughCalculation",
        "classicbar.cfg",
        "smoothfont",
        "placebo.cfg",
        "hud.txt"
    ]

    for f in files:
        if os.path.isdir(f):
            files.extend([os.path.join(f, ff) for ff in os.listdir(f) if ff not in dir_file_blacklist])
            
        if not silent_mode:
            print("Writing file: %s" % f)
        package.write(f, f)

    if not silent_mode:
        print("Writing file: readme.md")
    package.write(join(out_put_folder, "readme.md"), "readme.md")
    if not silent_mode:
        print("Writing file: readme.txt")
    package.write(join(out_put_folder, "readme.md"), "readme.txt")
    package.close()

def packup(parse_result:dict):
    _packup(parse_result.get('s', False))

class Services:

    def __init__(self):
        self._services = {}

    def get_service(self, service_name:str):
        service = self._services.get(service_name, None)
        if callable(service):
            return service
        else:
            raise KeyError("No such service `%s`" % service_name)
    
    def get_services_list(self):
        return self._services.keys()

    def register_service(self, name, f=None):
        if callable(name):
            self.register_service(name.__name__, name)
        if callable(f) and name not in self.get_services_list():
            self._services[name] = f


services = Services()
services.register_service(packup)

def make(parse_result):
    service = services.get_service(parse_result.get(0))
    service(parse_result)

if __name__ == "__main__":
    make(parse_all())



