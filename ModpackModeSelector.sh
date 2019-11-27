# /bin/bash

echo ==========================
echo 请选择modpack模式
echo ==========================
echo 服务器: s
echo 客户端: c
echo "单机端(默认): sp"
echo 开发端: d
echo 显示详细信息: h
echo ==========================
# ==============================================================================
find './mods' -maxdepth 1 | grep './mods/\[[C|D|S|L]\].*\.jar' | xargs -r --no-run-if-empty rm
# ==============================================================================

loop=1

while [ $loop -ne 0 ]
do
    loop=0
    client=0
    read -p '请输入模式代码: ' mode
    echo
    case $mode in
    'c')
        echo "您已选择: 客户端"
        cp ./mods/client/* ./mods/ 
        ;;
    'd')    
        echo "您已选择: 开发端"
        cp ./mods/dev/* ./mods/
        cp ./mods/sp_lan/* ./mods/ 
        cp ./mods/client/* ./mods/ 
        cp ./mods/server/* ./mods/
        ;;
    's')
        echo "您已选择: 服务端"
        cp ./mods/server/* ./mods/ 
        ;;
    'h')  
        echo "[s]  服务端:            服务端的mod配置"
        echo "[c]  客户端:            与服务端相对, 只可以链接服务端的mod配置"
        echo "[sp]单机端(默认):   可以进行单机游戏, 并可以与好友联机的mod配置(离线模式)"
        echo "[d]  开发端:           用于本mod包开发的mod配置"
        loop=1
        ;;
    *)
        echo "您已选择: 单机端"
        cp ./mods/sp_lan/* ./mods/ 
        cp ./mods/client/* ./mods/ 
        cp ./mods/server/* ./mods/
        ;;
    esac
done

echo "配置完毕"

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
else
	echo -e "$1"
fi
 
get_char
