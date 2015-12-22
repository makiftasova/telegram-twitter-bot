#!/usr/bin/bash
nohup python3 main.py > stdout.log 2> stderr.log &
echo $! > tg_bot.pid
