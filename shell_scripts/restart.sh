#/bin/bash

if [ $# -eq 0 ]
then
    echo "Usage: restart.sh <min_stable_running_time> [hiatus_time=10]"
    echo "  Auto-restart your program."
    echo "  Please put your program running commands in run.sh under the same directory with this script."
    echo "min_stable_running_time:"
    echo "  Minimum stable running time of the program you started in second(s)."
    echo "  If program run in ./run.sh terminated within this value, the program will not restart anymore."
    echo "hiatus_time:"
    echo "  Time between restarts in seconds"
    exit
fi
if [ ! -f ./run.sh ]
then
    echo "./run.sh not found!"
    echo "Please put your run commands in run.sh under the same directory with this script."
    exit
fi


min_time=$1
timer=10
if [ $# -eq 2 ]
then
    timer=$2
fi

start_time=0
end_time=$((${start_time} + ${min_time}))
run_time=$((${end_time} - ${start_time}))

while [ ${min_time} -le ${run_time} ]
do
    start_time=`date +%s`
    sh ./run.sh
    end_time=`date +%s`  
    run_time=$((${end_time}-${start_time}))
    if [ ${min_time} -le ${run_time} ]
    then
        echo "Program exit after ${run_time} secs, restart after ${timer} secs"
        while [ $timer -ge 0 ]
        do
            echo $timer
            timer=$(($timer-1))
            sleep 1s
        done
    fi
done
echo "! Program terminated within ${min_time} s"
echo "! Auto-restart stopped"
echo "! Please check log and/or crash report"