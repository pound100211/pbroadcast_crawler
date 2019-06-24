#########################################################################
# File Name: startall.sh
# Author: pyc
# mail: 
# Created Time: Mon 24 Jun 2019 11:10:02 AM CST
#########################################################################
#!/bin/bash
DATE=$(date +"%y%m%d%H%M%S")
nohup bash start.sh 001 zgzs & #>> #001zgzs${DATE}.log &
nohup bash start.sh 002 jjzs & #>> 002jjzs${DATE}.log &
nohup bash start.sh 003 yyzs & #>> 003yyzs${DATE}.log &
