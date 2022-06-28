#!/bin/bash

if [[ -n "$(pgrep swayrecorder)" && -n "$(pgrep wf-recorder)" ]]; then
    killall -s SIGINT wf-recorder | killall -s SIGINT swayrecorder
else
    swayrecorder
fi

