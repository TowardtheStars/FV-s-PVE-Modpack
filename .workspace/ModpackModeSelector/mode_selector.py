import os, sys, re


modes = {}

def add_mode(c, name, desc=None):

    modes[c] = (name, desc)

add_mode('c', '客户端', '进入服务器使用的模式')
add_mode('d', '开发端', '模组包开发使用的模式')
add_mode('l', '单机端', '进行单机游戏使用的模式')
add_mode('s', '服务器', '在服务器上运行时必选的模式')

def helper():
    print( "==========================")
    for k, v in modes.items():
        print(k+': '+v[0]+', '+v[1])
    print( "-help: 显示详细信息")
    print( "==========================")

if __name__ == "__main__":
    print( "==========================")
    print( "请选择modpack模式")
    helper()
    print("请输入模式代码: ")

    mode = sys.stdin.readline()[:-1]
    while mode not in modes.keys():
        if mode != '-help':
            print("请输入正确的模式代码")
        helper()
        mode = sys.stdin.readline()[:-1]
    
    print("转换为" + modes.get(mode)[0] + "模式")

    mod_path = os.path.join(".", "mods")
    for file in os.listdir(mod_path):
        if re.search("\[", file) :
            regex = "\[[^{mode}]*{mode}[^{mode}]*\].*\.jar".format(mode=mode)
            path = os.path.join(mod_path, file)
            if re.search(regex, file):
                os.rename(path, path.split('.jar')[0]+".jar")
            else:
                os.rename(path, path.split('.jar')[0]+'.jar.disabled')

    # For Windows
    print("模式转换完毕, 按回车退出...")
    sys.stdin.readline()

