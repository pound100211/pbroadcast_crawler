#########################################################################
# File Name: kill.sh
# Author: pyc
# mail: 
# Created Time: Mon 24 Jun 2019 11:18:08 AM CST
#########################################################################
#!/bin/bash


ps aux | grep script.py | grep -v grep |awk '{print $2}' | xargs -i kill -9 {}''


nohup bash 001zgzs/merge_video.sh &  
nohup bash ./002jjzs/merge_video.sh & 
nohup bash 003yyzs/merge_video.sh &  

