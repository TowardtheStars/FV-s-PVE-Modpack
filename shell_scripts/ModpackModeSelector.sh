# /bin/bash
if [ $# -eq 0 ]
then
echo "=========================="
echo "请选择modpack模式"
echo "=========================="
echo "客户端: c"
echo "开发端: d"
echo "单机端: l (默认)"
echo "服务器: s"
echo "显示详细信息: -help"
echo "=========================="
fi
# ==============================================================================

find './mods' -maxdepth 1 | 
    grep "\./mods/\[.*\.jar$" | 
    xargs -I {file} -n 1 -r mv {file} {file}.disabled

# ==============================================================================

loop=1
mode=sp
while [ $loop -ne 0 ]
do
    loop=0
    client=0
    if [ $# -eq 0 ]
    then 
        read -p '请输入模式代码: ' mode
        echo
    else 
    mode=$1
    fi
    case $mode in
    'c')
        if [ $# -eq 0 ]
        then echo "您已选择: 客户端"
        fi
        ;;
    's')
        if [ $# -eq 0 ]
        then echo "您已选择: 服务端"
        fi
        ;;
    'l')
        if [ $# -eq 0 ]
        then echo "您已选择: 单机端"
        fi
        ;;
    'd')
        if [ $# -eq 0 ]
        then echo "您已选择: 开发端"
        fi
        ;;
    *)  
        echo "[c]   客户端: 与服务端相对, 只可以链接服务端的mod配置"
        echo "[d]   开发端: 用于本mod包开发的mod配置"
        echo "[l]   单机端: 可以进行单机游戏, 并可以与好友联机的mod配置(离线模式) (默认)"
        echo "[s]   服务端: 服务端的mod配置"
        if [ $# -eq 0 ]
        then
            loop=1
        fi
        ;;
    esac

    if [ $loop -eq 0 ]
    then
        regex="\[[^$mode]*$mode[^$mode]*\].*\.jar\.disabled$"
        find './mods' -maxdepth 1 | 
            grep $regex | 
            xargs -n 1 -I {} -r echo {} | 
            sed 's/\.jar\.disabled/\.jar/g' | 
            xargs -n 1 -I {} -r mv {}.disabled {}
    fi
done

if [ $# -eq 0 ]
then echo "配置完毕"
fi

get_char()
{
  SAVEDSTTY=`stty -g`
  stty -echo
  stty raw
  dd if=/dev/tty bs=1 count=1 2> /dev/null
  stty -raw
  stty echo
  stty $SAVEDSTTY
}
 
if [ $# -eq 0 ]; then
	echo '请按任意键继续...'
    get_char
fi

