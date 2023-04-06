#!/bin/bash
sudo startx -- -nocursor &
sleep 1
export DISPLAY=:0
sudo xrandr --output HDMI-1 --rotate left
sudo java -jar DashBoard/Display.jar
