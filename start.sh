#########################################################################
# File Name: start.sh
# Author: pyc
# mail: 
# Created Time: Mon 24 Jun 2019 10:36:25 AM CST
#########################################################################
#!/bin/bash
if [ $# != 2 ]; then
	echo "script need 2 params!"
	echo "num & name"
	exit -1
fi

DATE=$(date +"%y%m%d%H%M%S")
NUM=$1
NAME=$2

if [ ! -d "${NUM}${NAME}" ];then
	mkdir ${NUM}${NAME}
fi
cd ${NUM}${NAME}

touch merge_video.sh
echo ffmpeg -f concat -safe 0 -i /home/pppppp/broadcast_recorder/${NUM}${NAME}/*.txt -c copy /home/pppppp/broadcast_recorder/${NUM}${NAME}/${NAME}${DATE}.mp4  >> merge_video.sh

cd ..
python script.py ${NUM} ${NAME}


