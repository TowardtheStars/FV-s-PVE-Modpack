#/bin/bash

echo "�뽫�����ű�������./run.sh��"
read -p "��������С�ȶ�����ʱ��(��λ: ��): " min_time

start_time=0
end_time=${start_time}+${time}

while [ $min_time -le `expr ${end_time} - ${start_time}` ]
do
    start_time=`date +%s`
    sh ./run.sh
    end_time=`date +%s`  
done
echo "! ����������ȶ�����ʱ������ֹ"
echo "! ֹͣ�Զ�����"
echo "! ��鿴log/crash report"