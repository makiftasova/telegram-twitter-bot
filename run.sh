#!/usr/bin/bash
nohup python3 main.py > bot.log 2>&1&
echo $! > save_pid.txt