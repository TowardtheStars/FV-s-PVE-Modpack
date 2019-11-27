#/bin/bash

echo "请将启动脚本放置于./run.sh中"
if [ $# -eq 0 ]
then
    read -p "请输入最小稳定运行时间(单位: 秒): " min_time
else
    min_time=$1
fi
start_time=0
end_time=${start_time}+${time}

while [ $min_time -le `expr ${end_time} - ${start_time}` ]
do
    start_time=`date +%s`
    sh ./run.sh
    end_time=`date +%s`  
done
echo "! 程序于最短稳定运行时间内(${min_time}s)终止"
echo "! 停止自动重启"
echo "! 请查看log和crash report"