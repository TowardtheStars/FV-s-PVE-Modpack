# /bin/bash
if [ $# -ne 1 ]
then
echo ==========================
echo 请选择modpack模式
echo ==========================
echo 服务器: s
echo 客户端: c
echo "单机端(默认): sp"
echo 开发端: d
echo 核心:   o
echo 显示详细信息: h
echo ==========================
fi
# ==============================================================================
find './mods' -maxdepth 1 | grep './mods/\[[C|D|S|L]\].*\.jar' | xargs -r --no-run-if-empty rm
# ==============================================================================

loop=1

while [ $loop -ne 0 ]
do
    loop=0
    client=0
    if [ $# -ne 1 ]
    then 
        read -p '请输入模式代码: ' mode
        echo
    else 
    mode=$1
    fi
    case $mode in
    'c')
        if [ $# -ne 1 ]
        then echo "您已选择: 客户端"
        fi
        cp ./mods/client/* ./mods/ 
        ;;
    'd')    
        if [ $# -ne 1 ]
        then echo "您已选择: 开发端"
        fi
        cp ./mods/dev/* ./mods/
        cp ./mods/sp_lan/* ./mods/ 
        cp ./mods/client/* ./mods/ 
        cp ./mods/server/* ./mods/
        ;;
    's')
        if [ $# -ne 1 ]
        then echo "您已选择: 服务端"
        fi
        cp ./mods/server/* ./mods/ 
        ;;
    'h')  
        echo "[s]  服务端:       服务端的mod配置"
        echo "[c]  客户端:       与服务端相对, 只可以链接服务端的mod配置"
        echo "[sp] 单机端(默认): 可以进行单机游戏, 并可以与好友联机的mod配置(离线模式)"
        echo "[d]  开发端:       用于本mod包开发的mod配置"
        echo "[o]  核心:         只保留以上所有端都包含的mod"
        loop=1
        ;;
    'o')
        if [ $# -ne 1 ]
        then echo "您已选择: 核心"
        fi
        ;;
    *)
        if [ $# -ne 1 ]
        then echo "您已选择: 单机端"
        fi
        cp ./mods/sp_lan/* ./mods/ 
        cp ./mods/client/* ./mods/ 
        cp ./mods/server/* ./mods/
        ;;
    esac
done

if [ $# -ne 1 ]
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
 
if [ -z "$1" ]; then
	echo '请按任意键继续...'
    get_char
fi
